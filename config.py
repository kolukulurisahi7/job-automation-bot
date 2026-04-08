"""Configuration for Nvoid Bot."""

# Search keywords and job matching
KEYWORDS = ["java", "spring", "backend", "microservices", "full stack"]
EXCLUDE_KEYWORDS = [
    "face to face",
    "f2f",
    "in person interview",
    "in-person interview",
    "face-to-face"
]  # Skip only these phrases

SEARCH_QUERIES = ["java"]  # Can add more queries like ["java", "python"]

# Email settings
MAX_EMAILS_PER_RUN = 25
DELAY_BETWEEN_EMAILS = 10
EMPLOYER_EMAIL = "dinesh@stemsolllc.com"

# Email extraction settings
EXCLUDE_DOMAINS = ["nvoids.com", "me@nvoids.com"]  # Exclude these from email picks
VALID_EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}"

# Browser settings
BROWSER_TIMEOUT = 20
JOB_PAGE_LOAD_TIME = 4
SEARCH_DELAY = 1

# Tracking
TRACKER_FILE = "applied_jobs.xlsx"
