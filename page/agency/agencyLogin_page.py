from utility.read_config import Read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class AngencyLogin():
    def __init__(self, browser):
        self.driver = browser
        self.content = Read_config().read_location_agency_login()

    def username_by(self):
        by = self.content['username']
        return by

    def ele_username(self):
        by = self.username_by()
        ele = WebDriverWait(self.driver, 30).until(ES.visibility_of_element_located(by))
        return ele

    def verification_by(self):
        by = self.content['verification']
        return by

    def ele_verification(self):
        by = self.verification_by()
        ele = self.driver.find_element(by[0], by[1])
        return ele

    def login_by(self):
        by = self.content['login']
        return by

    def ele_login(self):
        by = self.login_by()
        ele = self.driver.find_element(by[0], by[1])
        return ele