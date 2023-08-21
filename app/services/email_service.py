from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from ..config import settings
import jwt
from datetime import datetime, timedelta

SECRET_KEY =  settings.JWT_PRIVATE_KEY
TOKEN_EXPIRATION = timedelta(hours=24)

def send_email(subject, message, email):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = subject
    to = [{"email": email}]
    sender = {"name": "Speecho", "email": "no-reply@speecho.com"}
    html_content = f"<html><body><a href={message}>Sube tu audio</a></body></html>"
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        
def create_token(email):
    token = jwt.encode(
        {"email": email, "iat": datetime.utcnow()},
        SECRET_KEY,
        algorithm="HS256"
    )
    verification_link = f"http://localhost:5173/upload?token={token}"
    send_email(email=email, subject="Ahora puedes subir tu audio!", message=verification_link)
    return send_email