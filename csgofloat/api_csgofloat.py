import random
import time

from selenium.webdriver import ActionChains

from selenium_driver import BaseClass


class CSGOfloatApi(BaseClass):

    def __init__(self, user_data_dir):
        super(CSGOfloatApi, self).__init__()

        self.user_data_dir = user_data_dir
        self.DRIVER = self._driver(user_data_dir=self.user_data_dir)
        self.act = ActionChains(self.DRIVER)

    def auth_steam(self):
        self.click_element('//img[@src="assets/login-steam.png"]')
        time.sleep(3 * random.uniform(.2, .58))
        self.click_element('//input[@id="imageLogin"]')

    def prepare_db(self):
        self.DRIVER.get('https://csgofloat.com/')

        if self.xpath_exists('//img[@src="assets/login-steam.png"]'):
            self.auth_steam()

        self.DRIVER.get('https://csgofloat.com/db')

        time.sleep(20)
