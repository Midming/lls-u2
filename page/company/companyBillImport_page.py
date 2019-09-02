from utility.read_config import Read_config

class CompangyBillImport:
    def __init__(self,browser):
        self.driver = browser
        self.content = Read_config().read_location_company_billImport()
    def ele_full_time(self):
        by= self.content['full-time']
        print(by)
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def ele_part_time(self):
        by = self.content['part-time']
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def import_bill_by(self):
        by=self.content['import-bill']
        return by
    def ele_import_bill(self):
        by=self.import_bill_by()
        ele = self.driver.find_element(by[0], by[1])
        return ele
    def ele_import_bill_input(self):
        by=self.content['import-bill-input']
        ele = self.driver.find_element(by[0], by[1])
        return ele