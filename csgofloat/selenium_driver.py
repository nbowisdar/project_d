""" This file work with Selenium """
import random
import time

import undetected_chromedriver as uc

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self):
        self.DRIVER = None
        self.act = None

    def _driver(self,
                user_data_dir=None,
                browser_executable_path=None,
                headless=False,
                ):

        options = uc.ChromeOptions()

        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-backgrounding-occluded-windows")

        with uc.Chrome(
            options=options,
            user_data_dir=user_data_dir,
            browser_executable_path=browser_executable_path,
            headless=headless
        ) as self.DRIVER:

            self.DRIVER.maximize_window()
            self.act = ActionChains(self.DRIVER)

            return self.DRIVER, self.act

    def xpath_exists(self, xpath, wait=30):
        try:
            WebDriverWait(self.DRIVER, wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
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
            input(f"No found {xpath}")
