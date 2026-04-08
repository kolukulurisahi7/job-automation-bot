from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import config


def scrape_jobs(query="java"):
    """Scrape job listings from Nvoids."""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, config.BROWSER_TIMEOUT)

    try:
        driver.get("https://www.nvoids.com/index.jsp")

        print("Opening Nvoid site...")
        print("Page title:", driver.title)

        # optional: maximize window
        driver.maximize_window()

        # remove iframe ads if blocking
        driver.execute_script("""
            var frames = document.querySelectorAll("iframe");
            frames.forEach(f => {
                try {
                    f.remove();
                } catch(e) {}
            });
        """)

        # wait for search box
        search_box = wait.until(
            EC.element_to_be_clickable((By.ID, "search_id"))
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", search_box)
        time.sleep(config.SEARCH_DELAY)

        # clear old text
        search_box.clear()
        time.sleep(0.5)

        # use real typing first
        search_box.send_keys(query)
        print("Typed query:", query)
        time.sleep(config.SEARCH_DELAY)

        # find submit button
        submit_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit_btn)
        print("Clicked Submit")

        # wait for results page
        time.sleep(4)

        # collect only job detail links
        anchors = driver.find_elements(By.XPATH, "//a[contains(@href, 'job_details.jsp')]")

        jobs = []
        seen = set()

        for a in anchors:
            try:
                title = a.text.strip()
                href = a.get_attribute("href")

                if not title or not href:
                    continue

                if href in seen:
                    continue

                seen.add(href)
                jobs.append({
                    "title": title,
                    "link": href
                })
            except Exception as e:
                print(f"Error processing job element: {e}")
                continue

        print(f"Returning jobs: {len(jobs)}")
        return driver, jobs
    
    except Exception as e:
        print(f"Error scraping jobs: {e}")
        driver.quit()
        raise
