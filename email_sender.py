import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_USER, EMAIL_PASS, EMAIL_HOST, EMAIL_PORT


def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Email the specified recipient.

    :param to_email: Recipient's email address.
    :param subject: Subject of the email.
    :param body: Body of the email.
    """
    message = MIMEMultipart()
    message['From'] = EMAIL_USER
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to_email, message.as_string())
        print(f"Email sent to {to_email}.")
