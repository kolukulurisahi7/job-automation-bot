# Nvoid Bot

A Python automation tool that scrapes job postings from Nvoids, extracts recruiter emails, and creates Gmail drafts for relevant Java-related openings.

## Features

- Scrapes `https://www.nvoids.com` using Selenium
- Matches jobs by configurable keywords
- Skips duplicate jobs across runs
- Filters out F2F / face-to-face / in-person interview postings
- Extracts recruiter email addresses from job pages
- Creates Gmail drafts automatically
- Tracks processed jobs in `applied_jobs.xlsx`

## Project Structure

- `main.py` - main workflow: scrape jobs, parse details, create drafts, save tracker
- `nvoid_scraper.py` - search Nvoids and collect job links from results
- `job_parser.py` - open job page and extract emails and description
- `gmail_service.py` - authenticate with Gmail and create drafts
- `config.py` - central project settings and filters
- `test_gmail.py` - quick test script to verify Gmail draft creation
- `tracker.py` - tracker utilities (optional)
- `email_extractor.py` - email parsing utilities (optional)
- `scheduler/` - scheduler package placeholder

## Requirements

- Python 3.10+ (or compatible Python 3.x)
- Google Chrome installed
- ChromeDriver installed and available on `PATH`

## Python Dependencies

Install the required packages:

```bash
python -m pip install selenium openpyxl google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Setup

1. Clone or copy the repository into your workspace.
2. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install selenium openpyxl google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

4. Place `credentials.json` in the project root.
5. On first run, the script will open a browser window to authorize Gmail access and create `token.json`.

## Configuration

Edit `config.py` to customize behavior:

- `KEYWORDS` - job title keywords to include
- `EXCLUDE_KEYWORDS` - phrases to skip, such as F2F or face-to-face
- `SEARCH_QUERIES` - search terms used on Nvoids
- `MAX_EMAILS_PER_RUN` - limit drafts created per run
- `DELAY_BETWEEN_EMAILS` - delay between draft creations
- `EMPLOYER_EMAIL` - CC email for all drafts
- `EXCLUDE_DOMAINS` - email domains to avoid when picking recruiter emails

## Usage

Run the bot from the project root:

```bash
source venv/bin/activate
python main.py
```

The bot will:

1. Open Nvoids and search for the first query in `SEARCH_QUERIES`
2. Collect job links from the results
3. Evaluate each title for relevance
4. Open only relevant job pages and extract emails
5. Create Gmail drafts for valid recruiter emails
6. Save job history to `applied_jobs.xlsx`

## Troubleshooting

- If no drafts appear in Gmail:
  - Confirm the script authenticated the correct Gmail account
  - Delete `token.json` and rerun to reauthorize
  - Check `gmail_service.py` and `create_draft()` logs

- If Selenium cannot start:
  - Verify Chrome is installed
  - Install a matching ChromeDriver and add it to `PATH`

- If job pages stop parsing:
  - The Nvoids site structure may have changed
  - Update `job_parser.py` or `nvoid_scraper.py` accordingly

## Notes

- Drafts created before filter changes are not automatically removed.
- The bot uses both title and description matching to reduce false positives.
- Duplicate detection works by job ID, normalized title, and description signature.

## Optional Test

Run the Gmail test script to confirm the draft API:

```bash
python test_gmail.py
```

If you want, I can also add a `requirements.txt` and a `run.sh` script for easier setup.
