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
from selenium.webdriver.common.keys import Keys

from pykeyboard import PyKeyboard
from pymouse import PyMouse

from utility.utilities import ele_input,is_ele_exist
import time,pytest
from time import sleep


pt_bill_number=None
handle=None
Data_import_pt_bill=Read_config().read_pt_import_bill()
@pytest.fixture(scope='module',params=Data_import_pt_bill)
def data_import_pt_bill(request):
    return request.param

pt_bill_number=None
pt_bill_handle=None


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

class Test_agency():
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
        browser.maximize_window()
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

    def test_settlement_record(self,browser,pt_bill_number=None,pt_bill_handle=None):
        dashboard=self.page_dashboard(browser)
        dashboard.ele_home_page().click()
        browser.refresh()
        dashboard.ele_home_page().click()

        dashboard.ele_financial_management().click()
        dashboard.ele_settlement_record().click()
        time.sleep(3)

        sr=self.page_settlementRecord(browser)

        table_by=sr.table_by()
        table=sr.ele_table()
        rows=table.find_elements('tag name','tr')
        l_rows=len(rows)
        print('表格总行数{}'.format(l_rows))
        l_cols=len(rows[0].find_elements('tag name','td'))
        print('表格总列数{}'.format(l_cols))

        ele_total_num = browser.find_element('xpath', '//div[2]/div/span')
        total_num = ele_total_num.text
        total_num = total_num[2:-2]
        total_num = int(total_num)
        print('总的账单条数为{}'.format(total_num))
        a = (total_num // 10) + 1
        b = total_num % 10
        print('总页数为{}'.format(a))

        action = ActionChains(browser)
        non_pay_input_page = ['xpath',"//input[@type='number']"]
        for i in range(1, a + 1):
            ele_non_pay_input_page = browser.find_element(non_pay_input_page[0], non_pay_input_page[1])
            ele_non_pay_input_page.clear()
            ele_non_pay_input_page.send_keys('{}'.format(i))
            ele_non_pay_input_page.send_keys(Keys.ENTER)
            time.sleep(2)

            ele_table = browser.find_element(table_by[0], table_by[1])
            rows = ele_table.find_elements('tag name', 'tr')
            len_rows = len(rows)
            print('第{}页表格总行数{}'.format(i, len_rows))
            for j in range(len_rows):
                bill_num = rows[j].find_elements('tag name', 'td')[0]
                biii_num_text = bill_num.text
                # print('发现账单编号{}'.format(biii_num_text))
                if biii_num_text == pt_bill_number:
                    print('在第{}页的表格中的第{}行发现目标账单'.format(i, j + 1))
                    handle = rows[j].find_elements('tag name', 'td')[l_cols - 1]
                    print('定位账单记录成功')
                    action.move_to_element(handle).perform()
                    time.sleep(2)
                    selects = browser.find_elements('class name', 'el-dropdown-menu__item')
                    for e in selects:
                        if e.text == pt_bill_handle:
                            e.click()
                            time.sleep(2)
                            view_flow=['xpath','//div/button/span']
                            view_flow=browser.find_element(view_flow[0],view_flow[1])
                            assert view_flow.text=='查看结算流程'
                            return












        # for i in range(l_rows):
        #     bill_num=rows[i].find_elements('tag name','td')[0]
        #     if bill_num.text==pt_bill_number:
        #         print('该账单在第{}行'.format(i+1))
        #         h=rows[i].find_elements('tag name','td')[l_cols-1]
        #         # browser.execute_script("arguments[0].click();", h)
        #         action=ActionChains(browser)
        #         action.move_to_element(h).perform()
        #         time.sleep(1)
        #         selects=browser.find_elements('class name','el-dropdown-menu__item')
        #         for e in selects:
        #             if e.text==handle:
        #                 e.click()
        #                 break
        #     break

        # total_page=browser.find_element('xpath','//div[2]/div/span').text
        # total_page=int(total_page)
        # a=(total_page//10)+1
        # b=total_page%10








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







