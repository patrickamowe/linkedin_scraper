import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


def login_account(drive: uc.Chrome, email: str, password: str) -> None:
    """
    Automates the login process for a web application using Selenium.

    This function locates the username and password input fields,
    enters the provided credentials, and submits the login form.

    Parameters:
    drive (uc.Chrome): An active undetected Chrome WebDriver instance.
    email (str): The email or username used to log in.
    password (str): The account password.

    Returns:
    None
    """

    # Locate the username input field by its ID and enter the email
    username_input = drive.find_element(By.ID, "username")
    username_input.click()
    username_input.clear()
    username_input.send_keys(email)
    time.sleep(5)  # Wait to mimic human interaction and allow page stability

    # Locate the password input field by its ID and enter the password
    password_input = drive.find_element(By.ID, "password")
    password_input.click()
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(5)  # Pause before submitting the form

    # Locate the submit button using XPath and click it
    submit_btn = drive.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button')
    submit_btn.click()

