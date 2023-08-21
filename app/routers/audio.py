from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from ..config import settings
from ..services.audio_service import upload_file
import jwt

router = APIRouter()


@router.post("/upload/")
async def upload_audio(file: UploadFile = File(...), token: str = None):
    if not token:
        raise HTTPException(status_code=400, detail="Token missing")
    try:
        payload = jwt.decode(token, settings.JWT_PRIVATE_KEY, algorithms=["HS256"])
        email = payload["email"]
        
        to_transcript = upload_file(file)
        print(to_transcript)

        return FileResponse(path=to_transcript['path'], filename=to_transcript['filename'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token")
    except Exception as e:
        return e