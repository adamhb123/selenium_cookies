__author__ = "Adam Brewer"
"""
Loads and saves cookies to and from selenium drivers.

"""

import json
import time
from typing import Union
from datetime import datetime
from selenium import webdriver

class CookieHandler:
    def __init__(self, driver, main_page: Union[str, None], overwrite: bool = True, filename: str = 'lastsesh',
                 wait_time: int = 10):
        """
        Handles cookies for a given selenium webdriver.

        :param driver: Webdriver to handle cookies for.
        :param main_page: Page to load/save cookies on, some websites need this to function properly, others don't.
        Can be set to None if you don't want to use it.
        :param overwrite: Whether or not to overwrite the previously saved cookie file. If set to False, this creates
        a new file with the filename as the prefix and the date+time as the postfix.
        :param filename: Name of file to save cookies to (or if overwrite is False, the file prefix).
        :param wait_time: Time to wait for main_page to load. Only relevant if main_page is set to an actual webpage.
        """
        self.driver = driver
        self.main_page = main_page
        self.filename = filename
        self.wait_time = wait_time
        self.overwrite = overwrite
        self.loaded_cookies = None

    def load_cookies(self) -> Union[list, None]:
        """
        Loads cookies into the driver, stores them in self.loaded_cookies, and then returns them (or None on failure).

        :return: a list of the json-ed cookies (or None on failure)
        """
        if self.main_page is not None:
            self.driver.get(self.main_page)
            time.sleep(self.wait_time)
        cookies = []
        try:
            with open(self.filename + '.cookies', 'r') as f:
                lines = f.readlines()
                for cookie in lines:
                    cookie = json.loads(cookie)
                    cookies.append(cookie)
                    if self.driver is not None:
                        self.driver.add_cookie(cookie)
        except FileNotFoundError as e:
            print("There are no cookies to load!\nERROR: " + str(e))
            return None
        self.loaded_cookies = cookies
        return cookies

    def save_cookies(self) -> list:
        """
        Saves cookies into a file and returns a list of them.

        :return: a list of the cookies snagged from the driver
        """
        if self.main_page is not None:
            self.driver.get(self.main_page)
            time.sleep(self.wait_time)
        cookies = self.driver.get_cookies()
        #   Update self.filename to latest save if overwrite is disabled
        self.filename = self.filename if self.overwrite else self.filename + datetime.now().strftime(
            "d%m,%d,%Yt%H,%M,%S")
        with open(self.filename+'.cookies', 'w+') as f:
            for cookie in cookies:
                f.write(json.dumps(cookie) + '\n')

        return cookies
