import os,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pykeyboard import PyKeyboard
# from pymouse import PyMouse
import sys
# sys.path.append(os.getcwd())
print(sys.path)

user='15900545910'
password='952754'

# 元素定位
location={
    'username': ['name','phone'],
    'verification': ['name','smsCd'],
    'login': ['xpath',"//div[3]/div/button"],
    'home_page': ['css selector','[data-pup=CliIndexIndex]'],
    'financial_management': ['css selector','[data-pup=CliFinance]'],
    'settlement_record': ['css selector','[data-pup=CliFinanceSettlement]'],
    'table': ['xpath',"//div[@id='pane-first']/div/section[2]/div[2]/div[1]/div[3]/table"],
    'non_pay_input_page': ['xpath',"//input[@type='number']"]

}
# 登陆后的弹窗定位
window={
  'skip': ['xpath',"(.//*[normalize-space(text()) and normalize-space(.)='确 认'])[1]/following::span[2]"],
  'confirm': ['xpath','//button[2]/span']
}


browser=webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(5)
url='http://agency.test.shun178.com/#/login'

def is_ele_exist(browser,by):
    ele=None
    try:
        ele=browser.find_element(by[0],by[1])
    except NoSuchElementException:
        ele=False
    return ele

# 登陆操作
def test_login():
    browser.get(url)

    location_username=location['username']
    element_username=WebDriverWait(browser,30).until(ES.visibility_of_element_located(location_username))
    element_username.send_keys(user)

    location_verification=location['verification']
    browser.find_element(location_verification[0],location_verification[1]).send_keys(password)

    location_login=location['login']
    browser.find_element(location_login[0],location_login[1]).click()

    #处理登陆弹窗
    skip=window['skip']
    ele_window=is_ele_exist(browser,skip)
    if ele_window:
        print('发现弹窗')
        browser.find_element(skip[0],skip[1]).click()
        browser.find_element(window['confirm'][0],window['confirm'][1]).click()

    time.sleep(5)
    if browser.current_url=='http://agency.test.shun178.com/#/agency/dashboard':
        print('登陆成功')
    else:
        print('登陆失败')


# 点击【结算记录】模块中的操作选项，定位不了
def test_handle():
    location_home_page=location['home_page']
    browser.find_element(location_home_page[0],location_home_page[1]).click()

    browser.refresh()

    location_financial_management=location['financial_management']
    browser.find_element(location_financial_management[0],location_financial_management[1]).click()

    # 进入结算记录页面
    location_settlement_record=location['settlement_record']
    browser.find_element(location_settlement_record[0],location_settlement_record[1]).click()

    #定位表格
    location_table=location['table']
    ele_table=browser.find_element(location_table[0],location_table[1])

    rows = ele_table.find_elements('tag name', 'tr')
    len_rows = len(rows)
    print('表格总行数{}'.format(len_rows))
    len_cols = len(rows[0].find_elements('tag name', 'td'))
    print('表格总列数{}'.format(len_cols))

    # 简单点，我想点击第一条记录的操作字段的某一个选项
    # fist_row_handle=rows[0].find_elements('tag name', 'td')[len_cols-1]
    # action=ActionChains(browser)
    # action.move_to_element(fist_row_handle).perform()
    # time.sleep(2)

    # 定位表格中的某条记录，如账单编号为“201909060171”的记录
    # 比如我想点击这条记录的操作的【详情】，这个我就定位不到了
    ele_total_num=browser.find_element('xpath', '//div[2]/div/span')
    total_num = ele_total_num.text
    total_num=total_num[2:-2]
    total_num = int(total_num)
    print('总的账单条数为{}'.format(total_num))
    a = (total_num // 10) + 1
    b = total_num % 10
    print('总页数为{}'.format(a))
    current=1

    # fist_row=rows[len_rows-1].find_elements('tag name', 'td')[0]
    # print(fist_row.text)
    # action=ActionChains(browser)
    # action.move_to_element(ele_total_num).perform()
    # time.sleep(1)
    #
    # non_pay_input_page = location['non_pay_input_page']
    # ele_non_pay_input_page = browser.find_element(non_pay_input_page[0], non_pay_input_page[1])
    # ele_non_pay_input_page.clear()
    # ele_non_pay_input_page.send_keys('2')
    # ele_non_pay_input_page.send_keys(Keys.ENTER)

    action = ActionChains(browser)
    non_pay_input_page = location['non_pay_input_page']

    for i in range(1,a+1):

        ele_non_pay_input_page = browser.find_element(non_pay_input_page[0], non_pay_input_page[1])
        ele_non_pay_input_page.clear()
        ele_non_pay_input_page.send_keys('{}'.format(i))
        ele_non_pay_input_page.send_keys(Keys.ENTER)
        time.sleep(2)


        ele_table = browser.find_element(location_table[0], location_table[1])
        rows = ele_table.find_elements('tag name', 'tr')
        len_rows = len(rows)
        print('第{}页表格总行数{}'.format(i, len_rows))
        for j in range(len_rows):
            bill_num = rows[j].find_elements('tag name', 'td')[0]
            biii_num_text=bill_num.text
            print('发现账单编号{}'.format(biii_num_text))
            if biii_num_text=='201908300157':
                print('在第{}页的表格中的第{}行发现目标账单'.format(i,j+1))
                handle = rows[j].find_elements('tag name', 'td')[len_cols - 1]
                print('定位账单记录成功')
                action.move_to_element(handle).perform()
                time.sleep(2)
                selects=browser.find_elements('class name','el-dropdown-menu__item')
                for e in selects:
                    if e.text=='详情':
                        e.click()
                        time.sleep(2)
                        view_flow = ['xpath', '//div/button/span']
                        view_flow = browser.find_element(view_flow[0], view_flow[1])
                        assert view_flow.text == '查看结算流程'
                        break
                break







                # e=browser.find_element('xpath', '/html/body/ul/li')
                # print(e.text)
                # e.click()
                # break

    # for i in range(len_rows):
    #     bill_num = rows[i].find_elements('tag name', 'td')[0]
    #     print(bill_num.text)
    #     if bill_num.text == '201909030169':
    #         # 定位记录的操作字段
    #         handle = rows[i].find_elements('tag name', 'td')[len_cols - 1]
    #         print('定位账单记录成功')
    #
    #
    #
    #         # 点击操作字段按钮，弹出操作选项（通过find_element定位报错：元素被遮挡）
    #         action = ActionChains(browser)
    #         action.move_to_element(handle).perform()
    #         time.sleep(2)
    #
    #         e=browser.find_element('xpath', '/html/body/ul/li')
    #         print(e.text)
    #         e.click()
    #         break






            # selects=browser.find_elements('class name','el-dropdown-menu__item')
            # for e in selects:
            #     print(e.text)
            #     if e.text=='详情':
            #         e.click()
            #         break


            # hover_master = browser.find_elements_by_class_name('el-dropdown-menu')
            # for master in hover_master:
            #     print(master.text)
            #     # if master.text  == "详情":
            #     #     master.click()

# 下面就该定位操作选项了如详情，我定位不到了？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？







if __name__ == '__main__':
    test_login()
    test_handle()
    # time.sleep(3)
    # browser.quit()



