from selenium import webdriver
import pytest

driver='chrome'
@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    if driver==None or driver=="chrome":
        driver=webdriver.Chrome()
    if driver=='firefox':
        driver=webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver
# @pytest.fixture(scope='session',autouse=True)
# def close_browser():
#     yield driver
#     driver.quit()
#     msg='测试正常结束，自动关闭浏览器'
#     print(msg)

