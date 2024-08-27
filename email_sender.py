from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import SEND_GRID_API_CLIENT, FROM_EMAIL


def send_email(to_email: str, subject: str, body: str) -> None:
    """
    Email the specified recipient using SendGrid.

    :param to_email: Recipient's email address.
    :param subject: Subject of the email.
    :param body: Body of the email.
    """

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content=body)
    try:
        sg = SendGridAPIClient(SEND_GRID_API_CLIENT)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)
