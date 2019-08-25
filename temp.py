import os,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utility.utilities import ele_input
from selenium.webdriver.support import expected_conditions as ES

from urllib.parse import urljoin
url='http://platform.test.shun178.com/#/login'
driver=webdriver.Chrome()
driver.get(url)

by=['name','phone']
ele_uname=WebDriverWait(driver,20).until(ES.visibility_of_element_located(by))
ele_input(ele_uname,'18917965476')

by=['name','smsCd']
ele_uv = driver.find_element(by[0], by[1])
ele_input(ele_uv,'952754')

ele=driver.find_element('xpath','//div[3]/div/button/span')
ele.click()
vv="//div[@id='app']/div/div/div/div[3]/span/button/span"
by=['xpath',vv]
ele=WebDriverWait(driver,20).until(ES.visibility_of_element_located(by))
print(driver.title)
print(driver.current_url)
print(driver.name)
print(ele.text)
ele.click()
time.sleep(5)
driver.close()
# wangyi='163.com'S
# ba=u+baidu
# wa=u+wangyi
# driver=webdriver.Chrome()S
# driver.implicitly_wait()
# driver.get('http://platform.test.shun178.com/#/login')
# driver.find_element('name','phone').send_keys('21')
# class a():
#     def __init__(self,driver):
#         self.driver=driver
#     def a1(self):
#         self.driver.get(ba)
# class b():
#     def __init__(self,driver):
#         self.driver=driver
#     def b1(self):
#         self.driver.get(wa)
# a(driver).a1()
# b(driver).b1()
# d={'a':{'a1':1.1,'a':1.2},'b':'2'}
# v=d.values()
# print(type(v),v)
# w='a2'
# for i in v:
#     if w in i:
#         c=i[w]
#         print(i)
#         print(c)
