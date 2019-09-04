from utility.read_config import Read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class CompanyDashboard():
    def __init__(self, browser):
        self.driver = browser
        self.content = Read_config().read_location_company_dashboard()

    def window_by(self):
        by=self.content['window']['self']
        return by
    def ele_window(self):
        by=self.window_by()
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_window_confirm(self):
        by = self.content['window']['confirm']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_home_page(self):
        by=self.content['home_page']
        ele = self.driver.find_element(by[0], by[1])
        return ele

    def ele_settlement_management(self):
        by=self.content['settlement-management']
        ele = self.driver.find_element(by[0], by[1])
        return ele

    def ele_bill_import(self):
        by=self.content['bill-import']
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def ele_settlement_record(self):
        by=self.content['settlement-record']
        ele = self.driver.find_element(by[0], by[1])
        return ele


