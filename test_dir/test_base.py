from utility.read_config import Read_config
from page.platform.platformLogin_page import PlatformLogin
from page.agency.agencyLogin_page import AngencyLogin
from page.agency.agencyDashboard_page import AgencyDashboard
from page.agency.agencySettlementRecord_page import AgencySettlementRecord

from page.company.companyLogin_page import CompanyLogin
from page.company.companyDashboard_page import CompanyDashboard
from page.company.companyBillImport_page import CompangyBillImport
from page.company.companySettlementDetails_page import CompangySettlementDetails

from selenium.webdriver import ActionChains

from utility.utilities import ele_input,is_ele_exist
import time,pytest
from time import sleep


pt_bill_number=None
Data_import_pt_bill=Read_config().read_pt_import_bill()
@pytest.fixture(scope='module',params=Data_import_pt_bill)
def data_import_pt_bill(request):
    return request.param




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
    def page_login(self,browser):
        eles=AngencyLogin(browser)
        return eles
    def page_dashboard(self,browser):
        eles=AgencyDashboard(browser)
        return eles
    def page_settlementRecord(self,browser):
        eles=AgencySettlementRecord(browser)
        return eles

    def test_login(self,browser):
        rd = Read_config()

        role = rd.angency_role('tester01')
        url=rd.angency_url('login')
        self.page_login(browser).driver.get(url)
        username = role[0]
        verification = role[1]
        ele_username = self.page_login(browser).ele_username()
        ele_input(ele_username, username)

        ele_verification = self.page_login(browser).ele_verification()
        ele_input(ele_verification, verification)

        ele_login = self.page_login(browser).ele_login()
        ele_login.click()

        dashboard=self.page_dashboard(browser)
        window_by=dashboard.window_by()
        ele_window=is_ele_exist(browser,window_by)
        if ele_window:
            print('发现弹窗')
            ele_window.click()
            dashboard.ele_window_confirm().click()


        url_dashboard = rd.angency_url('dashboard')
        time.sleep(3)
        assert_url = self.page_login(browser).driver.current_url

        print(url_dashboard, assert_url)
        assert url_dashboard == assert_url

    def test_settlement_record(self,browser):
        ds=self.page_dashboard(browser)
        ds.ele_home_page().click()
        browser.refresh()
        ds.ele_home_page().click()

        ds.ele_financial_management().click()
        ds.ele_settlement_record().click()
        time.sleep(5)
        sr=self.page_settlementRecord(browser)
        table=sr.ele_table()
        rows=table.find_elements('tag name','tr')
        l_rows=len(rows)
        print('表格总行数{}'.format(l_rows))
        l_cols=len(rows[0].find_elements('tag name','td'))

        print('表格总列数{}'.format(l_cols))


        for i in range(l_rows):
            bill_num=rows[i].find_elements('tag name','td')[0]
            if bill_num.text=='201909030168':
                h=rows[i].find_elements('tag name','td')[l_cols-1]
                # browser.execute_script("arguments[0].click();", h)
                ActionChains(browser).move_to_element(h).perform()
                break









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
        assert url_dashboard == assert_url


    @pytest.mark.skip(reason='跳过')
    def test_part_time_bill(self,browser,data_import_pt_bill):
        rd = self.readconifg()
        dashboard=CompanyDashboard(browser)
        browser.refresh()
        dashboard.ele_home_page().click()
        browser.refresh()
        dashboard.ele_settlement_management().click()
        dashboard.ele_bill_import().click()
        # dashboard.ele_settlement_record().click()


        page_billImport=CompangyBillImport(browser)
        page_billImport.ele_part_time().click()
        bill_part_time=rd.get_bill_part_time(data_import_pt_bill)
        filepath = bill_part_time[0]
        expect=bill_part_time[1]
        ele_pt_import_bill_input=page_billImport.ele_pt_import_bill_input()
        ele_pt_import_bill_input.send_keys(filepath)
        if expect:
            ele_pt_import_success=page_billImport.ele_pt_import_success()
            ele_pt_import_success.click()

            msg=ele_pt_import_success.text

            page_settlementDeatails=CompangySettlementDetails(browser)
            try:
                ele_pt_bill_number = page_settlementDeatails.ele_pt_bill_number()
            except Exception:
                print('获取导入的非全日制账单编号失败')
            else:
                global pt_bill_number
                pt_bill_number=ele_pt_bill_number.text
                print('导入的非全日制账单成功，编号为{}'.format(pt_bill_number))
            assert msg=='查看结算单'
        else:
            time.sleep(1)
            ele_pt_import_fail=page_billImport.ele_pt_import_fail()
            msg=ele_pt_import_fail.text
            page_billImport.ele_pt_import_fail_close().click()
            time.sleep(1)
            assert msg=='重新导入'







