# Selenium Cookie Handler

## What does it do?
Saves and loads cookies from a given selenium webdriver.

## Why?
Useful for storing user information amongst other things. This is 
actually ripped from my myNotifsV2 project where I save & load cookies in
order to automatically log the user in rather than having them log 
in every single time they run the application. 

## Installation
```bash
pip install selenium_cookies
```
## Usage
```python
from selenium import webdriver
from selenium_cookies import CookieHandler
dummy_driver = webdriver.Firefox()
#   The second argument is the page to go to when saving/loading cookies.
#   In some cases this is necessary for the loading and saving of cookies
#   to actually work. If you don't have this issue, you can just set it to None.
cookie_handler = CookieHandler(dummy_driver,"https://github.com/adamhb123/selenium_cookies", 
                               overwrite=False, filename="cooks", wait_time=5)
#   save_cookies() saves the site cookies to the specified file
saved_cookies = cookie_handler.save_cookies()
#   load_cookies() loads the saved cookies from the given file (or from the most recently saved one)
loaded_cookies = cookie_handler.load_cookies()
print("Saved cookies == loaded cookies == cookie_handler.loaded_cookies: " + str(
        saved_cookies == loaded_cookies == cookie_handler.loaded_cookies))
```
Should you so choose, there is also a basic test available in selenium_cookies.tests:
```python
from selenium import webdriver
from selenium_cookies.tests import test_module
dummy_driver = webdriver.Firefox() # could also be webdriver.Chrome()
#   If the driver argument is not supplied, test_module.test attempts to create
#   the webdriver.Firefox instance with the locally stored geckodriver (0.27.0).  
test_module.test(driver=dummy_driver)
```