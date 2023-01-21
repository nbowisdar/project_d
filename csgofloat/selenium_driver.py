""" This file work with Selenium """
import os
import time
import random

import undetected_chromedriver as uc

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self):
        self.DRIVER = None

    def __set_new_download_path(self, download_path):

        # Defines autodownload and download PATH
        params = {
            "behavior": "allow",
            "downloadPath": download_path
        }
        self.DRIVER.execute_cdp_cmd("Page.setDownloadBehavior", params)

        return self.DRIVER

    def _driver(self, profile=None, browser_executable_path=None, user_data_dir=None, download_path="default"):
        """
        Call driver via undetected_driver;

        if you pass user_data_dir:
            profile: user_data_dir(the most correct and safe way)

        elif you pass profile:
            profile: your (Profile num)
            Your profile is passed through chrome's option

        else:
            driver opens the incognito webpages and deletes cookies.
            Then you can use authorization on the YouTube

        return: driver
        """

        your_options = {}

        options = uc.ChromeOptions()

        # need for working on the backgrounding
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-backgrounding-occluded-windows")

        if user_data_dir is not None:
            your_options["user_data_dir"] = user_data_dir

        elif profile is not None:
            # match on windows 10
            options.add_argument(fr"--user-data-dir={os.environ['USERPROFILE']}\AppData\Local\Google\Chrome\User Data")
            options.add_argument(f"--profile-directory={profile}")

        your_options["options"] = options
        your_options["browser_executable_path"] = browser_executable_path

        # if not profile or user_data_dir == incognito
        self.DRIVER = uc.Chrome(**your_options)

        self.DRIVER.maximize_window()

        # if you need download to your folder
        if download_path == "default":
            return self.DRIVER

        else:
            return self.__set_new_download_path(download_path)

    def xpath_exists(self, xpath, wait=30, return_xpath=False):
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            take_xpath = WebDriverWait(self.DRIVER,
                                       wait,
                                       ignored_exceptions=ignored_exceptions
                                       ).until(EC.presence_of_element_located((By.XPATH, xpath)))

            if not return_xpath:
                return True
            else:
                # retrurn
                return take_xpath

        except TimeoutException:
            return False

    def click_element(self, xpath, wait=60):
        try:
            WebDriverWait(self.DRIVER, wait).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            return True
        except TimeoutException:
            return False

    def send_text_by_elem(self, xpath, text_or_key):

        if self.click_element(xpath):
            research_xpath = self.DRIVER.find_element(By.XPATH, xpath)
            research_xpath.clear()
            research_xpath.send_keys(text_or_key)

        else:
            input(f"No found or no be clickable {xpath}")

    def refrash_page(self):
        """if you have "Not Found data" call this function"""
        time.sleep(random.uniform(.58, 1))
        self.DRIVER.refresh()
        self.DRIVER.reconnect(random.uniform(2, 5.8))
