from utility.read_config import Read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class AgencyDashboard():
    def __init__(self, browser):
        self.driver = browser
        self.content = Read_config().read_location_agency_dashboard()
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
        ele=self.driver.find_element(by[0],by[1])
        return ele


    def ele_client_management(self):
        by=self.content['client_management']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_demander(self):
        by=self.content['demander']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_service_provider(self):
        by=self.content['service_provider']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_bill_confirm(self):
        by=self.content['bill_confirm']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_financial_management(self):
        by=self.content['financial_management']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_settlement_record(self):
        by=self.content['settlement_record']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_transaction_data(self):
        by=self.content['transaction_data']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_withdraw_record(self):
        by=self.content['withdraw_record']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_system_mangement(self):
        by=self.content['system_mangement']
        ele=self.driver.find_element(by[0],by[1])
        return ele
    def ele_user_management(self):
        by=self.content['user_management']
        ele=self.driver.find_element(by[0],by[1])
        return ele
