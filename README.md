#Selenium Cookie Handler
##What does it do?
Saves and loads cookies from a given selenium webdriver.
##Why?
Useful for storing user information amongst other things. This is 
actually ripped from my myNotifsV2 project where I save cookies in
order to automatically log the user in rather than having them log 
in every single time they run the application. 
##Installation
```bash
pip install selenium_cookies
```
##Usage
```python
from selenium import webdriver
from selenium_cookies import CookieHandler
dummy_driver = webdriver.Firefox()
#   The second argument is the page to go to when saving/loading cookies.
#   In some cases this is necessary for the loading and saving of cookies
#   to actually work. If you don't have this issue, you can just set it to None.
cookie_handler = CookieHandler(dummy_driver,"https://github.com/adamhb123/selenium_cookies", 
                               overwrite=False, filename="cooks.cookies", wait_time=)
#   save_cookies() returns the site cookies, stores them in cookie_handler.loaded_cookies, 
#   and saves them to a file whose default name is 
cookies = cookie_handler.save_cookies()
```