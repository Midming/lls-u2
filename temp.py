import os,time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from utility.utilities import ele_input
from selenium.webdriver.support import expected_conditions as ES
url='https://www.baidu.com/'
driver=webdriver.Chrome()
driver.get(url)
