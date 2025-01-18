
import smtplib
import re
from email.message import EmailMessage
from typing import Optional

def send_email(to_email: str, subject: str, message: str) -> Optional[None]:
    """
    Send an email using SMTP
    """
    if not re.match(r"[^@]+@[^@]+\.[^@]+", to_email):
        raise ValueError("Invalid email address")

    msg = EmailMessage()
    msg.set_content(message)
    
    msg['Subject'] = subject
    msg['From'] = "noreply@admission-ai.com"
    msg['To'] = to_email

    try:
        with smtplib.SMTP('localhost', 1025) as server:
            server.send_message(msg)
        return None
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")
