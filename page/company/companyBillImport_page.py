from utility.read_config import Read_config

class CompangyBillImport:
    def __init__(self,browser):
        self.driver = browser
        self.content = Read_config().read_location_company_billImport()
    def ele_full_time(self):
        by= self.content['full-time']
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def ele_part_time(self):
        by = self.content['part-time']
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def pt_import_bill_input_by(self):
        by=self.content['pt-import-bill-input']
        return by
    def ele_pt_import_bill_input(self):
        by=self.pt_import_bill_input_by()
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def ele_pt_import_success(self):
        by=self.content['pt-import-success']
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def ele_pt_import_fail(self):
        by=self.content['pt_import_fail']
        ele = self.driver.find_element(by[0], by[1])
        return ele
