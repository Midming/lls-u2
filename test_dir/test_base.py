from utility.read_config import Read_config
from page.platform.platformLogin_page import PlatformLogin
from page.agency.agencyLogin_page import AngencyLogin
from page.agency.agencyDashboard_page import AgencyDashboard

from page.company.companyLogin_page import CompanyLogin
from page.company.companyDashboard_page import CompanyDashboard
from page.company.companyBillImport_page import CompangyBillImport


from utility.utilities import ele_input,is_ele_exist
import time
from time import sleep

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

        # ele_after_login_assert=self.platform(browser).ele_after_login_assert()
        # if ele_after_login_assert.text!="暂不绑定？点此跳过":
        #     msg='登陆失败'
        #     print(msg)
        # if 1:
        #     print(self.platform(browser).driver.title)
        # ele_after_login_assert.click()
        url_dashboard=rd.platform_url('dashboard')
        time.sleep(3)
        assert_url=self.platform(browser).driver.current_url
        print(url_dashboard,assert_url)
        assert url_dashboard==assert_url

class Test_agecy():
    def elements(self,browser):
        eles=AngencyLogin(browser)
        return eles

    def test_login(self,browser):
        rd = Read_config()

        role = rd.angency_role('tester01')
        url=rd.angency_url('login')
        self.elements(browser).driver.get(url)
        username = role[0]
        verification = role[1]
        ele_username = self.elements(browser).ele_username()
        ele_input(ele_username, username)

        ele_verification = self.elements(browser).ele_verification()
        ele_input(ele_verification, verification)

        ele_login = self.elements(browser).ele_login()
        ele_login.click()

        dashboard=AgencyDashboard(browser)
        window_by=dashboard.window_by()
        ele_window=is_ele_exist(browser,window_by)
        if ele_window:
            print('发现弹窗')
            ele_window.click()
            dashboard.ele_window_confirm().click()


        url_dashboard = rd.angency_url('dashboard')
        time.sleep(3)
        assert_url = self.elements(browser).driver.current_url

        print(url_dashboard, assert_url)
        assert url_dashboard == assert_url

class Test_company():
    @staticmethod
    def readconifg():
        rd = Read_config()
        return rd
    def elements(self,browser):
        eles=CompanyLogin(browser)
        return eles

    def test_login(self,browser):
        rd=self.readconifg()
        role = rd.company_role('tester01')
        url=rd.company_url('login')
        self.elements(browser).driver.get(url)
        username = role[0]
        verification = role[1]
        ele_username = self.elements(browser).ele_username()
        ele_input(ele_username, username)

        ele_verification = self.elements(browser).ele_verification()
        ele_input(ele_verification, verification)

        ele_login = self.elements(browser).ele_login()
        ele_login.click()

        dashboard=CompanyDashboard(browser)
        window_by=dashboard.window_by()
        ele_window=is_ele_exist(browser,window_by)
        if ele_window:
            print('发现弹窗')
            ele_window.click()
            dashboard.ele_window_confirm().click()


        url_dashboard = rd.company_url('dashboard')
        time.sleep(3)
        assert_url = self.elements(browser).driver.current_url

        print(url_dashboard, assert_url)
        assert url_dashboard == assert_url
    def get_part_time_bill(self):


    def test_part_time_bill(self,browser):
        rd = self.readconifg()

        dashboard=CompanyDashboard(browser)
        dashboard.ele_settlement_management().click()
        sleep(1)
        dashboard.ele_bill_import().click()
        sleep(1)
        page_billImport=CompangyBillImport(browser)
        page_billImport.ele_part_time().click()
        sleep(1)
        # page_billImport.ele_full_time().click()
        # sleep(1)
        ele_import_bill=page_billImport.ele_import_bill()
        filepath=rd.get_bill_part_time()
        ele_import_bill_input=page_billImport.ele_import_bill_input()
        ele_import_bill_input.send_keys(filepath)







