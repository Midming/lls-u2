from utility.read_config import Read_config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

class AgencySettlementRecord:
    def __init__(self, browser):
        self.driver = browser
        self.content = Read_config().read_location_agency_settlementRecord()

    def table_by(self):
        by = self.content['table']
        return by

    def ele_table(self):
        by = self.table_by()
        print(by)
        ele = self.driver.find_element(by[0],by[1])
        return ele