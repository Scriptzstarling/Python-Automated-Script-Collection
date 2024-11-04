import smtplib
from email.mime.text import MIMEText
import getpass  # import getpass module

def send_email(sender_email, receiver_email, subject, message, password):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Collect input from the user
sender_email = input("Enter your email address: ")
password = getpass.getpass("Enter your email password: ")  # hides password input
receiver_email = input("Enter the receiver's email address: ")
subject = input("Enter the subject of the email: ")
message = input("Enter the message you want to send: ")

# Send the email
send_email(sender_email, receiver_email, subject, message, password)
