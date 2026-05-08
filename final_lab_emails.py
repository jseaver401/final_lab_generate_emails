#!/usr/bin/env python3
import smtplib
import mimetypes
import os.path
from email.message import EmailMessage

def generate_email(sender, recipient, subject, body, attachment_path=None):
    message = EmailMessage()
    message["From"], message["To"], message["Subject"] = sender, recipient, subject
    message.set_content(body)
    
    if attachment_path:
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        with open(attachment_path, "rb") as ap:
            message.add_attachment(ap.read(), maintype=mime_type, 
                                   subtype=mime_subtype, filename=os.path.basename(attachment_path))
    return message

def send_email(message):
    with smtplib.SMTP('localhost') as mail_server:
        mail_server.send_message(message)