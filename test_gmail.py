from gmail_service import get_gmail_service, create_draft

service = get_gmail_service()

create_draft(
    service,
    "your_email@gmail.com",
    "Test Draft from Bot",
    "Hello, this is a test draft from Nvoid Bot."
)

print("Draft created successfully!")