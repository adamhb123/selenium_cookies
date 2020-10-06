from selenium_cookies import CookieHandler
from selenium import webdriver


#   Test utilizes Firefox 81.0 and Geckodriver 0.27.0
#   Geckodriver is included, Firefox is not
def test(driver):
    if driver is None:
        driver = webdriver.Firefox()
    cookie_handler = CookieHandler(driver,'https://github.com/adamhb123/selenium_cookies')
