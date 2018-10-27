import sys
import re
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/javascript-alert-box-demo.html')
driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[1]/div[2]/button').click()
time.sleep(5)
obj = driver.switch_to.alert
time.sleep(5)
obj.accept()
driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()
time.sleep(5)
obj1 = driver.switch_to.alert
time.sleep(5)
obj1.accept()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button').click()
time.sleep(5)
obj1 = driver.switch_to.alert
time.sleep(5)
obj1.dismiss()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="easycont"]/div/div[2]/div[3]/div[2]/button').click()
time.sleep(5)
obj1 = driver.switch_to.alert
#time.sleep(5)
obj1.send_keys('python program')
time.sleep(5)
obj1.accept()
time.sleep(10)
driver.close()
