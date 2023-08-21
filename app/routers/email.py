from fastapi import FastAPI, APIRouter
from ..services.email_service import create_token

app = FastAPI()

router = APIRouter()

    
@router.post("/submit-email")
def submit_email(email: dict = {}):
    to = email["email"]
    verification_link = create_token(to)
    print(verification_link)
    return {"message": "Email submitted. Check your email for the upload link."}

