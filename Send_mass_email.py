# import os
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Read SMTP server configuration from environment variables
# smtp_server = "smtp.gmail.com"
# smtp_port = 587
# # smtp_username = "anujshakya808@gmail.com"
# # smtp_password = "uqvy eara tefy uhvr"  #it will generate from app passwords(Google account->app password)
# smtp_username = os.getenv("SMTP_USERNAME")
# smtp_password = os.getenv("SMTP_PASSWORD")

# # Email content
# subject = "Send the mass messages to multiple email ids"
# body = "This is the body of the email."

# # List of recipient email addresses
# recipients = ["anujjj004@gmail.com", "ankitshakya16@gmail.com", "ritiksingh150@gmail.com"]

# def send_email(smtp_server, smtp_port, smtp_username, smtp_password, recipient, subject, body):
#     try:
#         # Create the email
#         msg = MIMEMultipart()
#         msg['From'] = smtp_username
#         msg['To'] = recipient
#         msg['Subject'] = subject

#         msg.attach(MIMEText(body, 'plain'))

#         # Connect to the SMTP server
#         print(f"Connecting to SMTP server {smtp_server} on port {smtp_port}...")
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         server.ehlo()
#         server.starttls()

#         # Log in to the server
#         print(f"Logging in as {smtp_username}...")
#         server.login(smtp_username, smtp_password)

#         # Send the email
#         print(f"Sending email to {recipient}...")
#         server.sendmail(smtp_username, recipient, msg.as_string())

#         # Disconnect from the server
#         server.quit()
#         print(f"Email sent successfully to {recipient}")
#     except Exception as e:
#         print(f"Failed to send email to {recipient}: {str(e)}")

# if smtp_username and smtp_password:
#     # Send email to each recipient
#     for recipient in recipients:
#         send_email(smtp_server, smtp_port, smtp_username, smtp_password, recipient, subject, body)
# else:
#     print("SMTP_USERNAME and SMTP_PASSWORD environment variables must be set.")


import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Read SMTP server configuration from environment variables
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "anujshakya808@gmail.com"
smtp_password = "uqvy eara tefy uhvr" 

# Verify environment variables are set
if not smtp_username or not smtp_password:
    print("SMTP_USERNAME and SMTP_PASSWORD environment variables must be set.")
    exit()

# Email content
subject = "Your Subject"
body = "This is the body of the email."

# Read the list of recipient email addresses from a CSV file
recipients_file = 'recipients.csv'
try:
    df = pd.read_csv(recipients_file)
    recipients = df['email'].tolist()
except Exception as e:
    print(f"Failed to read the CSV file: {str(e)}")
    exit()

def send_email(smtp_server, smtp_port, smtp_username, smtp_password, recipient, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        print(f"Connecting to SMTP server {smtp_server} on port {smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()

        # Log in to the server
        print(f"Logging in as {smtp_username}...")
        server.login(smtp_username, smtp_password)

        # Send the email
        print(f"Sending email to {recipient}...")
        server.sendmail(smtp_username, recipient, msg.as_string())

        # Disconnect from the server
        server.quit()
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {str(e)}")

# Send email to each recipient
for recipient in recipients:
    send_email(smtp_server, smtp_port, smtp_username, smtp_password, recipient, subject, body)
