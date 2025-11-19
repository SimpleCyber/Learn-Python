import streamlit as st
import pandas as pd
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load environment variables (e.g., email credentials)
load_dotenv()

# Email credentials (these should be set in a .env file)
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

st.title("Multi-User Email Sender")

# Upload email list file
uploaded_file = st.file_uploader("Upload your email list (Excel, TXT, etc.)", type=["xlsx", "csv", "txt", "pdf"])

email_list = []

if uploaded_file:
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        email_list = df.iloc[:, 0].tolist()  # Assuming emails are in the first column
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        email_list = df.iloc[:, 0].tolist()
    elif uploaded_file.type == "text/plain":
        email_list = uploaded_file.read().decode("utf-8").splitlines()
    elif uploaded_file.type == "application/pdf":
        st.write("PDF format is not supported yet. Please upload a different format.")
else:
    st.write("No file uploaded yet.")

# Add emails manually
manual_emails = st.text_area("Add emails manually (separate with commas)")
if manual_emails:
    email_list += [email.strip() for email in manual_emails.split(",")]

st.write("Emails to send to:")
st.write(email_list)

# Email content
subject = st.text_input("Email Subject")
message = st.text_area("Email Body")

# File attachments
attachments = st.file_uploader("Attach files", accept_multiple_files=True)

# Review the message
if st.button("Review Message"):
    st.write("Subject: ", subject)
    st.write("Message: ", message)
    if attachments:
        st.write("Attachments:")
        for attachment in attachments:
            st.write(attachment.name)

# Send email function
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
        part.add_header('Content-Disposition', f"attachment; filename= {attachment.name}")
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
        st.error(f"Failed to send email to {recipient}: {e}")
        return False

# Send the emails
if st.button("Send Emails"):
    success_count = 0
    for email in email_list:
        if send_email(email, subject, message, attachments):
            success_count += 1
    st.success(f"Emails sent successfully to {success_count} out of {len(email_list)} recipients.")

