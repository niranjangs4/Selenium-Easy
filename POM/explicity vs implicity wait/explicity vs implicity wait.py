from Locators.elements import *
from libs_utils.web_launch import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = visit(r'file:///C:/Users/niran/Downloads/Ajax.html')

driver.find_element_by_xpath('/html/body/button').click()

element = WebDriverWait(driver, 10)

element.until(EC.text_to_be_present_in_element((By.ID, 'div4'), 'fourth'))
element.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'div4'), 'fourth'))

print(element)

time.sleep(5)

driver.close()
