import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .selenium_driver import BaseClass


class CSGOfloatApi(BaseClass):

    def __init__(self, user_data_dir):
        super(CSGOfloatApi, self).__init__()

        self.user_data_dir = user_data_dir
        self.DRIVER, self.act = self._driver(
            user_data_dir=self.user_data_dir
        )

    def auth_csgofloat(self):
        self.DRIVER.get('https://csgofloat.com/')

        time.sleep(6 * random.uniform(.2, .58))

        self.DRIVER.get('https://csgofloat.com/db')

    def __send_float_value(self, item):
        self.send_text_by_elem('//input[@formcontrolname="min"]', item["float_value"])
        time.sleep(5 * random.uniform(.2, .58))

        self.send_text_by_elem('//input[@formcontrolname="max"]', item["float_value"])

    def __second_send_float_value(self, item):
        # fix round "float_value" if exists drag settings for float_value
        if self.xpath_exists('//nouislider'):
            self.__send_float_value(item["float_value"])
            time.sleep(5 * random.uniform(.2, .58))

    def __paint_seed_send(self, item):
        self.send_text_by_elem('//input[@formcontrolname="paintSeed"]', item["paint_seed"])
        time.sleep(5 * random.uniform(.2, .58))

    def __filling_filter(self, item):
        # clear
        self.click_element('//button[@mattooltip="Clear Search Parameters"]')

        # uncaptcha
        funcs = [self.__paint_seed_send, self.__send_float_value, self.__second_send_float_value]
        for fun in random.sample(funcs, len(funcs)):
            fun(item)

        # name
        if item["name"] != "-":
            self.send_text_by_elem('//input[@formcontrolname="name"]', item["name"])
            time.sleep(2 * random.uniform(.2, .58))

        # press button "Search"
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

    def get_links(self, item, filter=True):

        if filter:
            self.__filling_filter(item)

        # exists item in table
        if self.xpath_exists('//tbody'):
            # exists profile not market
            if self.xpath_exists('//*[contains(text(), "Knife")]/ancestor::tr//a[contains(@class, "playerAvatar")]'):

                # open and switch new tab
                self.DRIVER.tab_new(
                    self.DRIVER.find_element(By.XPATH,
                                             '//*[contains(text(), "Knife")]/ancestor::tr//a[contains(@class, "playerAvatar")]').get_attribute(
                        "href")
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

        elif self.xpath_exists('//*[contains(text(), "failed to verify recaptcha - 116")]'):

            time.sleep(5 * random.uniform(.2, .58))
            self.DRIVER.refresh()
            self.DRIVER.reconnect(5 * random.uniform(2, 5.8))

            return self.get_links(item, filter=False)

        else:
            return "NotFound", "NotFound"
