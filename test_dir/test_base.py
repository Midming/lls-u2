from page.platformLogin_page import PlatformLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ES
from utility.read_config import Read_config
from page.platformLogin_page import PlatformLogin
from utility.utilities import ele_input
import os
import time

class Test_platform:

    def platform(self,browser):
        p=PlatformLogin(browser)
        return p

    def test_login(self,browser):
        rd=Read_config()
        role=rd.platform_role('tester01')

        url = rd.platform_url('login')
        self.platform(browser).driver.get(url)
        username=role[0]
        verification=role[1]
        ele_username=self.platform(browser).ele_username()
        ele_input(ele_username,username)

        ele_verification=self.platform(browser).ele_verification()
        ele_input(ele_verification,verification)

        ele_login=self.platform(browser).ele_login()
        ele_login.click()

        ele_after_login_assert=self.platform(browser).ele_after_login_assert()
        if ele_after_login_assert.text!="暂不绑定？点此跳过":
            msg='登陆失败'
            print(msg)
        if 1:
            print(self.platform(browser).driver.title)
        ele_after_login_assert.click()


    # @classmethod
    # def teardown_class(cls):







