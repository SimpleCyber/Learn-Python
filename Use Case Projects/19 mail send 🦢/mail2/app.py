# app.py
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Email credentials
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Send Email Route
@app.route('/send_emails', methods=['POST'])
def send_emails():
    email_file = request.files.get('email_file')
    manual_emails = request.form.get('manual_emails', '')
    subject = request.form.get('subject')
    message = request.form.get('message')
    attachments = request.files.getlist('attachments')

    email_list = []

    if email_file:
        filename = secure_filename(email_file.filename)
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext == '.xlsx':
            df = pd.read_excel(email_file)
            email_list = df.iloc[:, 0].tolist()
        elif file_ext == '.csv':
            df = pd.read_csv(email_file)
            email_list = df.iloc[:, 0].tolist()
        elif file_ext == '.txt':
            email_list = email_file.read().decode("utf-8").splitlines()
        else:
            return "Unsupported file format.", 400

    if manual_emails:
        email_list += [email.strip() for email in manual_emails.split(",")]

    success_count = 0
    for recipient in email_list:
        if send_email(recipient, subject, message, attachments):
            success_count += 1

    return f"Emails sent successfully to {success_count} out of {len(email_list)} recipients."

# Send Email Function
def send_email(recipient, subject, message, attachments):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    for attachment in attachments:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment.filename}")
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL, recipient, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")
        return False

if __name__ == '__main__':
    app.run(debug=True)
