import time
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from auth.login import login_account

load_dotenv() # load environment variables

# your linkedin login details
email = os.getenv("EMAIL_ADDRESS", default=None)
password = os.getenv("PASSWORD", default=None)

driver = uc.Chrome()
driver.get("https://www.linkedin.com/")
time.sleep(10)

login_btn = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.linkedin.com/login"]')
login_btn.click()

# Logging in to your linkedin account
login_account(driver, email, password)

time.sleep(10)

driver.close()

