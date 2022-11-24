import random
import time

from loguru import logger
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .selenium_driver import BaseClass


class CSGOfloatApi(BaseClass):

    def __init__(self, user_data_dir):
        super(CSGOfloatApi, self).__init__()

        self.user_data_dir = user_data_dir
        self.DRIVER = self._driver(user_data_dir=self.user_data_dir)
        self.act = ActionChains(self.DRIVER)

    def __prepare_steam(self):
        if self.click_element('//img[@src="assets/login-steam.png"]'):
            # open steam new tab
            time.sleep(random.uniform(.2, .58))
            self.DRIVER.execute_cdp_cmd("Target.createTarget",
                                        {"url": "https://store.steampowered.com/", "newWindow": False})
            # switch new tab
            self.DRIVER.switch_to.window(self.DRIVER.window_handles[-1])
            time.sleep(3 * random.uniform(.2, .58))

            # go to steam's profile
            self.click_element('//div[@id="global_header"]//a[@data-tooltip-content=".submenu_username"]')
            self.xpath_exists('//div[@id="global_header"]//a[@data-tooltip-content=".submenu_username"]')
            self.DRIVER.reconnect(10 * random.uniform(.2, .58))

            # close and switch tabs
            self.DRIVER.close()
            self.DRIVER.switch_to.window(self.DRIVER.window_handles[0])

            # reboot webpage
            self.DRIVER.refresh()
            self.DRIVER.reconnect(10 * random.uniform(.2, .58))
            # auth through steam
            self.click_element('//input[@id="imageLogin"]')

    def auth_csgofloat(self):
        self.DRIVER.get('https://csgofloat.com/')

        self.__prepare_steam()
        time.sleep(6 * random.uniform(.2, .58))

        self.DRIVER.get('https://csgofloat.com/db')

