import imaplib
import time
from email.message import EmailMessage

EMAIL_ADDRESS = "kolukulurisahi7@gmail.com"
EMAIL_PASSWORD = "vibzjvixyqgqjhd"  # Use Gmail App Password, NOT your regular password


def create_gmail_draft(recipients, subject, body):
    if not EMAIL_ADDRESS or EMAIL_ADDRESS == "your_email@gmail.com":
        raise ValueError("Please update EMAIL_ADDRESS")

    if not EMAIL_PASSWORD or EMAIL_PASSWORD == "your_16_char_app_password":
        raise ValueError("Please update EMAIL_PASSWORD (use Gmail App Password)")

    if not recipients:
        raise ValueError("No recipient email provided")

    if isinstance(recipients, list):
        recipients = ", ".join(recipients)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipients
    msg.set_content(body, charset="utf-8")

    raw_message = msg.as_bytes()

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Try Gmail Drafts folder
        result = mail.append(
            "[Gmail]/Drafts",
            "\\Draft",
            imaplib.Time2Internaldate(time.time()),
            raw_message
        )

        # Fallback if folder name differs
        if result[0] != "OK":
            result = mail.append(
                "Drafts",
                "\\Draft",
                imaplib.Time2Internaldate(time.time()),
                raw_message
            )

        if result[0] != "OK":
            raise RuntimeError(f"Failed to create draft: {result}")

        mail.logout()
        print(f"📝 Gmail draft created for: {recipients}")

    except imaplib.IMAP4.error as e:
        raise ValueError(f"Gmail login failed: {e}")
    except Exception as e:
        raise RuntimeError(f"Failed to create Gmail draft: {e}")
