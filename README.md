### Speecho API ###
## Versión 0.0.1 ##

Speecho es una aplicación que transcribe notas de audio en español, entregando un archivo *.docx con el texto extraido. Para
esta API utilizamos:

[Whisper](https://github.com/openai/whisper)
[FastAPI](https://fastapi.tiangolo.com/)
[Brevo](https://www.brevo.com/)

Y para futuras implementaciones:

[SQLAlchemy](https://www.sqlalchemy.org/)
[PostgresSQL](https://www.postgresql.org/)
[Docker](https://www.docker.com/)

Versión 0.0.1:

- Implementación básica de autorización con token JWT y Brevo.
- Almacenamiento de archivos de forma temporal.

Por desarrollar:

- Creación y gestión de usuarios.
- Almacenamiento de datos de las transcripciones realizadas por cada usuario.
- Mejorar formato del archivo *.docx con texto de transcripción.

