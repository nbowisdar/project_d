import random
import time

from selenium.webdriver.common.by import By

from .selenium_driver import BaseClass


class CSGOfloatApi(BaseClass):

    def __init__(self, user_data_dir):
        super(__class__, self).__init__()

        self.user_data_dir = user_data_dir

    def __enter__(self):
        self.DRIVER = self._driver(user_data_dir=self.user_data_dir)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.DRIVER.quit()

    def auth_csgofloat(self):
        self.DRIVER.get('https://csgofloat.com/')

        # wait while not loading page
        self.xpath_exists('//body')

        # Not AUTH on the steam !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__auth_steam()

        self.DRIVER.get('https://csgofloat.com/db')

    def __auth_steam(self):
        if self.click_element('//img[@src="assets/login-steam.png"]', 1):
            # open steam new tab
            time.sleep(random.uniform(.2, .58))
            self.DRIVER.tab_new("https://store.steampowered.com/")

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

    def __send_float_value(self, float_value):
        self.send_text_by_elem('//input[@formcontrolname="min"]', float_value)
        time.sleep(2 * random.uniform(.2, .58))

        self.send_text_by_elem('//input[@formcontrolname="max"]', float_value)
        time.sleep(2 * random.uniform(.2, .58))

    def __paint_seed_send(self, paint_seed):
        self.send_text_by_elem('//input[@formcontrolname="paintSeed"]', paint_seed)
        time.sleep(5 * random.uniform(.2, .58))

    def __filling_filter(self, item):
        # clear
        self.click_element('//button[@mattooltip="Clear Search Parameters"]')

        self.__paint_seed_send(item["paint_seed"])

        self.__send_float_value(item["float_value"])

        # fix round "float_value" if exists drag settings for float_value
        if self.xpath_exists('//nouislider'):
            self.__send_float_value(item["float_value"])

        # name
        if item["name"] != "-":
            self.send_text_by_elem('//input[@formcontrolname="name"]', item["name"])
            time.sleep(2 * random.uniform(.2, .58))

        # press button "Search"
        self.click_element('//mat-spinner-button/button')

    def __get_url_account(self, already_exists=False):

        if self.xpath_exists('//div[@class="profile_small_header_texture"]/a'):
            return self.DRIVER.find_element(By.XPATH,
                                            '//div[@class="profile_small_header_texture"]/a'
                                            ).get_attribute("href")
        else:
            if not already_exists:
                self.__get_url_account(already_exists=True)
            else:
                print("This idea not working for Steam, if after this massege not get link on the account")

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
            self.refrash_page()

            return self.get_links(item, filter=False)

        return "NotFound", "NotFound"



# project_d
# pyinstaller -y -F -n csgo -i csgo.ico runer_tg.py --hidden-import csgofloat --path C:\Users\Username\PycharmProjects\project_d\venv\Lib\site-packages