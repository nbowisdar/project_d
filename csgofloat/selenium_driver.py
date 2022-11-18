""" This file work with Selenium """

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:

    def __init__(self):
        self.DRIVER = None

    def _driver(self,
                user_data_dir=None,
                browser_executable_path=None,
                headless=False,
                ):

        with uc.Chrome(
                user_data_dir=user_data_dir,
                browser_executable_path=browser_executable_path,
                headless=headless
                ) as self.DRIVER:

            self.DRIVER.maximize_window()

        return self.DRIVER

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

    def send_some_by_elem(self, xpath, element):

        if self.xpath_exists(xpath):
            self.DRIVER.find_element(By.XPATH, xpath).send_keys(element)
        else:
            input(f"No found {xpath}")
