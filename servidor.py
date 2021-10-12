# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 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

# save this as app.py
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/correo")
def enviarCorreo():
    destino = request.args.get("destino")
    asunto = request.args.get("asunto")
    mensaje = request.args.get("mensaje")
    hashString = request.args.get("hash")
    if  hashString == os.environ.get("SECURITY_HASH"):
        message = Mail(
            from_email=os.environ.get("email_from"),
            to_emails=destino,
            subject=asunto,
            html_content=mensaje)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("enviado")
            return "OK"
        except Exception as e:
            print(e.message)
            return "KO"
    else:
        print("Hash error")
        return "KO"

if __name__ == "__main__":
    app.run()