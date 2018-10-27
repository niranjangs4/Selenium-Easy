import sys
import os
from selenium.webdriver import ActionChains
sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/bootstrap-dual-list-box-demo.html')
element_left = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div/ul')
for no,i in enumerate(element_left.find_elements_by_class_name('list-group-item'),start=1):
    print(no,i.text)
print('\n\n')
element_right = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/ul')
for no,i in enumerate(element_right.find_elements_by_class_name('list-group-item'),start=1):
    print(no,i.text)


driver.find_element_by_xpath('//*[@id="listhead"]/div[1]/div/input').send_keys('boot')


driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div/ul/li[1]').click()

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/button[2]').click()


for no,i in enumerate(element_right.find_elements_by_class_name('list-group-item'),start=1):
    print(no,i.text)
driver.close()