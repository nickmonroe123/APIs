from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
from flask_cors import CORS
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
CORS(app)  # This will enable CORS for all routes


def send_email(subject, message, from_addr, to_addr, smtp_server, smtp_port, username, password):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()


class SendEmail(Resource):
    def get(self):
        send_email(
            subject="Hello!",
            message="This is a test email.",
            from_addr="nickmonroe1998@outlook.com",
            to_addr="nickmonroe1998@outlook.com",
            smtp_server="smtp-relay.brevo.com",
            smtp_port=587,
            username=os.getenv('EMAIL_USERNAME'),
            password=os.getenv('EMAIL_PASSWORD')
        )

        return jsonify({"text": "Good Call"})


api.add_resource(SendEmail, "/send_email")

if __name__ == "__main__":
    app.run(debug=True)





