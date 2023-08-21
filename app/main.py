from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

description = """
### Descripción ###
Transcripción de notas de audio en español, utilizando FastAPI y whisper.ai para el backend.

### Instrucciones ###
1.- Introducir un email válido en el endpoint *submit-email*. A este email se le enviará un link con el token necesario para poder
cargar un archivo de audio.

2.- Copiar el token del link enviado y pegarlo en el endpoint *upload*. Cargar un archivo de nota de voz en español en el mismo endpoint
y ejecutar.

### Aplicación completa ###

Esta API funciona mejor en conjunto con el frontend desarrollado en Vue.js.


#### Desarrollado por [Pag0dy](https://github.com/pag0dy)

"""

app = FastAPI(
    title="Speecho API",
    description=description
)

origins = ["http://localhost:5173", "http://localhost:5174"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routers
from app.routers.audio import router as audio_router
app.include_router(audio_router, prefix="/api/audio", tags=["audio"])

from app.routers.email import router as email_router
app.include_router(email_router, prefix="/api/email", tags=["email"])

