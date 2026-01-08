'''
'''

from abc import abstractmethod, ABC

class EmailClient(ABC):
    @abstractmethod
    def send_email(self, to, subject, body):
        pass

class GmailClientImpl(EmailClient):
    def send_email(self, to, subject, body):
        print("Connecting to Gmail SMTP server...")
        print(f"Sending email via Gmail to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # ... actual Gmail API interaction logic ...
        print("Gmail email sent successfully!")

class OutlookClientImpl(EmailClient):
    def send_email(self, to, subject, body):
        print("Connecting to Outlook Exchange server...")
        print(f"Sending email via Outlook to: {to}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        # ... actual Outlook API interaction logic ...
        print("Outlook email sent successfully!")

class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_welcome_email(self, user_email, user_name):
        subject = f"Welcome, {user_name}!"
        body = "Thanks for signing up to our awesome platform. We're glad to have you!"
        self.email_client.send_email(user_email, subject, body)

    def send_password_reset_email(self, user_email):
        subject = "Reset Your Password"
        body = "Please click the link below to reset your password..."
        self.email_client.send_email(user_email, subject, body)

if __name__ == "__main__":
    print("--- Using Gmail ---")
    gmail_service = EmailService(GmailClientImpl())
    gmail_service.send_welcome_email("test@example.com", "Welcome to SOLID principles!")

    print("\n--- Using Outlook ---")
    outlook_service = EmailService(OutlookClientImpl())
    outlook_service.send_welcome_email("test@example.com", "Welcome to SOLID principles!")
