from utility.read_config import Read_config
from utility.basePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES


class PlatformLogin:
    def __init__(self,browser):
        self.driver=browser
        self.platform=Read_config().location_login()['platform']

    def username_by(self):
        by=self.platform['username']
        return by
    def ele_username(self):
        by=self.username_by()
        ele=WebDriverWait(self.driver,30).until(ES.visibility_of_element_located(by))
        return ele

    def verification_by(self):
        by=self.platform['verification']
        return by
    def ele_verification(self):
        by=self.verification_by()
        ele=self.driver.find_element(by[0],by[1])
        return ele

    def login_by(self):
        by=self.platform['login']
        return by
    def ele_login(self):
        by=self.login_by()
        ele=self.driver.find_element(by[0],by[1])
        return ele

    def ele_after_login_assert(self):
        by=['xpath', "//div[@id='app']/div/div/div/div[3]/span/button/span"]
        ele=WebDriverWait(self.driver,30).until(ES.visibility_of_element_located(by))
        return ele









