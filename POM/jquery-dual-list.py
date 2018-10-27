import sys
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html')
options_left = Select(driver.find_element_by_xpath('//*[@id="pickList"]/div/div[1]/select'))
for no,x in enumerate(options_left.options,start=1):
    print(no,x.text)
    if no >5:
        options_left.select_by_visible_text(x.text)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pickList"]/div/div[2]/button[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="pickList"]/div/div[2]/button[4]').click()
time.sleep(5)
driver.close()

