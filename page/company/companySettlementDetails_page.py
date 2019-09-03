from utility.read_config import Read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class CompangySettlementDetails:
    def __init__(self,browser):
        self.driver = browser
        self.content = Read_config().read_location_company_settlementDetails()
    def ele_pt_bill_number(self):
        by= self.content['pt-bill-number']
        ele = self.driver.find_element(by[0], by[1])
        return ele