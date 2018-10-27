import sys
import re
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/window-popup-modal-demo.html')
print(driver.window_handles)
driver.find_element_by_link_text('Follow On Twitter').click()
time.sleep(5)

print(driver.window_handles)


driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_id('username_or_email').send_keys('niranjan')
driver.find_element_by_id('password').send_keys('1234')
driver.find_element_by_id('remember').click()
driver.find_element_by_xpath('//*[@id="follow-login-form"]/fieldset[2]/input').click()
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.close()