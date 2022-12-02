import random
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from .selenium_driver import BaseClass


class CSGOfloatApi(BaseClass):

    def __init__(self, user_data_dir):
        super(CSGOfloatApi, self).__init__()

        self.user_data_dir = user_data_dir
        self.DRIVER, self.act = self._driver(
            user_data_dir=self.user_data_dir,
            browser_executable_path=uc.find_chrome_executable()
        )

    def auth_csgofloat(self):
        self.DRIVER.get('https://csgofloat.com/')

        time.sleep(6 * random.uniform(.2, .58))

        self.DRIVER.get('https://csgofloat.com/db')

    def __send_float_value(self, value):
        self.send_text_by_elem('//input[@formcontrolname="min"]', value)

        self.send_text_by_elem('//input[@formcontrolname="max"]', value)

    def __filling_filter(self, item):
        self.click_element('//button[@mattooltip="Clear Search Parameters"]')

        self.send_text_by_elem('//input[@formcontrolname="paintSeed"]', item["paint_seed"])
        time.sleep(3 * random.uniform(.2, .58))

        self.__send_float_value(item["float_value"])
        time.sleep(2 * random.uniform(.2, .58))

        # fix round "float_value" if exists drag settings for float_value
        if self.xpath_exists('//nouislider'):
            self.__send_float_value(item["float_value"])
            time.sleep(2 * random.uniform(.2, .58))

        if item["name"] != "-":
            self.send_text_by_elem('//input[@formcontrolname="name"]', item["name"])
            time.sleep(3 * random.uniform(.2, .58))

        self.click_element('//mat-spinner-button/button')

    def __get_url_account(self):

        self.xpath_exists('//div[@class="profile_small_header_texture"]/a')

        return self.DRIVER.find_element(By.XPATH,
                                        '//div[@class="profile_small_header_texture"]/a'
                                        ).get_attribute("href")

    def __get_trade_link(self):
        self.xpath_exists('//body')

        # click "Подробнее" on the steam account
        self.click_element('//div[contains(@class, "profile_summary_footer")]', wait=2)

        # find trade in title steam profile
        if self.xpath_exists('//*[contains(@href, "/tradeoffer") and @target="_blank"]', wait=3):
            return self.DRIVER.find_element(
                By.XPATH, '//*[contains(@href, "/tradeoffer") and @target="_blank"]'
            ).get_attribute('href')

    def get_links(self, item):
        self.__filling_filter(item)

        # exists item in table
        if self.xpath_exists('//tbody', wait=5):
            # exists profile not market
            if self.xpath_exists('//a[@class="playerAvatar offline"]', wait=2):
                # open and switch new tab
                self.DRIVER.tab_new(
                    self.DRIVER.find_element(By.XPATH, '//a[@class="playerAvatar offline"]').get_attribute("href")
                )
                self.DRIVER.switch_to.window(self.DRIVER.window_handles[-1])

                # get url profile
                url_account = self.__get_url_account()

                # to go main page profile
                self.DRIVER.get(url_account)
                trade_link = self.__get_trade_link()

                # close and switch tabs
                self.DRIVER.close()
                self.DRIVER.switch_to.window(self.DRIVER.window_handles[0])

                return url_account, trade_link

        return None, None
