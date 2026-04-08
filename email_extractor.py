import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

BLOCKED_EMAILS = {
    "me@nvoids.com",
    "usjobs@nvoids.com",
}

def extract_emails(text: str):
    found = re.findall(EMAIL_REGEX, text or "")
    cleaned = []

    for email in found:
        email = email.strip().lower()

        if email in BLOCKED_EMAILS:
            continue

        if email not in cleaned:
            cleaned.append(email)

    return cleaned