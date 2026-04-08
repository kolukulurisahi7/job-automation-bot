import re
import time
from selenium.webdriver.common.by import By
import config


def is_valid_email(email):
    """Validate email format."""
    pattern = config.VALID_EMAIL_PATTERN
    return re.match(pattern, email) is not None


def extract_emails(text):
    """Extract and validate emails from text."""
    emails = list(set(re.findall(
        config.VALID_EMAIL_PATTERN,
        text
    )))
    
    # Filter out invalid emails and common junk patterns
    valid_emails = []
    for email in emails:
        email_lower = email.lower()
        
        # Skip if matches excluded domains
        if any(excluded in email_lower for excluded in config.EXCLUDE_DOMAINS):
            continue
        
        # Skip obviously invalid emails
        if email_lower.endswith('.'):
            continue
        
        # Skip emails with consecutive dots
        if '..' in email_lower:
            continue
            
        if is_valid_email(email):
            valid_emails.append(email)
    
    return valid_emails


def parse_job(driver, job):
    """Parse job details from job posting page."""
    url = job.get("link")
    
    if not url:
        print("No URL found for job")
        return {
            "emails": [],
            "phones": [],
            "description": ""
        }

    try:
        driver.execute_script("window.open(arguments[0]);", url)
        time.sleep(config.JOB_PAGE_LOAD_TIME)

        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(config.JOB_PAGE_LOAD_TIME)

        text = driver.find_element(By.TAG_NAME, "body").text
        html = driver.page_source

        emails = extract_emails(text) + extract_emails(html)
        emails = list(set(emails))  # Remove duplicates

        print("DEBUG preview:", text[:300])
        print("DEBUG emails:", emails)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        return {
            "emails": emails,
            "phones": [],
            "description": text
        }
    
    except Exception as e:
        print(f"Error parsing job page: {e}")
        try:
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except:
            pass
        
        return {
            "emails": [],
            "phones": [],
            "description": ""
        }