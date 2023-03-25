import time
from utils.urls import login_url
from utils.creds import get_credentials
from utils.exceptions import AuthorizationException


def auth_login(driver):
    """Logs in to the meetup website using the credentials from the auth_info file"""
    email, password = get_credentials()
    driver.get(login_url)
    driver.find_element("name", "email").send_keys(email)
    driver.find_element("name", "current-password").send_keys(password)
    driver.find_element("name", "submitButton").click()
    time.sleep(10)
    if driver.current_url == login_url:
        raise AuthorizationException()
