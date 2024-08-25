import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


def send_email(subject: str, body: str, to_email: str, from_email: str, password: str, smtp_server: str, smtp_port: int) -> None:
    """
    Send an email with the given subject and body to the specified recipient.

    :param subject: The subject of the email.
    :param body: The body of the email.
    :param to_email: The recipient's email address.
    :param from_email: The sender's email address.
    :param password: The password for the sender's email account.
    :param smtp_server: The SMTP server address.
    :param smtp_port: The port to use for the SMTP server.
    """

    # Create the email headers and body
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body text
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(from_email, password)  # Login to the server
            server.sendmail(from_email, to_email, message.as_string())  # Send the email
            print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main() -> None:
    """
    Main function to load environment variables and send a 'Hello, World!' email.
    """

    # Load environment variables from .env file
    load_dotenv()

    # Gather email credentials and recipient information from environment variables
    from_email: str = os.getenv('EMAIL_USER', '')
    password: str = os.getenv('EMAIL_PASS', '')
    smtp_server: str = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    smtp_port: int = int(os.getenv('EMAIL_PORT', 587))
    to_email: str = 'sdat0004@student.monash.edu'

    # Define the subject and body of the email
    subject: str = "Hello, World!"
    body: str = "Hello, World!"

    # Send the email
    send_email(subject, body, to_email, from_email, password, smtp_server, smtp_port)


if __name__ == "__main__":
    main()
