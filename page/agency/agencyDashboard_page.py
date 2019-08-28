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