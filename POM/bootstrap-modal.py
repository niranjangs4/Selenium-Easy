import sys
import re
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/bootstrap-modal-demo.html')

button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a')
button.click()
# time.sleep(5)
element = WebDriverWait(driver, 10)

print(element.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[3]/a'))))
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[3]/a').click()
print(element.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[6]/a[2]'))))
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[6]/a[2]').click()

time.sleep(3)
driver.close()
