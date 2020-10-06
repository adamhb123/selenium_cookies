from typing import Union
from selenium_cookies import CookieHandler
from selenium import webdriver


#   Test utilizes Firefox 81.0 and Geckodriver 0.27.0
#   Geckodriver is included, Firefox is not
def test(driver: Union[webdriver.Firefox, webdriver.Chrome, None] = None):
    if driver is None:
        driver = webdriver.Firefox(executable_path='./geckodriver')
    cookie_handler = CookieHandler(driver, 'https://github.com/adamhb123/selenium_cookies')
    saved_cookies = cookie_handler.save_cookies()
    loaded_cookies = cookie_handler.load_cookies()
    print(saved_cookies)
    print(loaded_cookies)
    print("Saved cookies == loaded cookies == cookie_handler.loaded_cookies: " + str(
        saved_cookies == loaded_cookies == cookie_handler.loaded_cookies))

    assert saved_cookies == loaded_cookies == cookie_handler.loaded_cookies


if __name__ == "__main__":
    test()
