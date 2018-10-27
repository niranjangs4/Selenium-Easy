from Locators.elements import *
from libs_utils.web_launch import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
driver = visit(r"C:\Users\niran\Downloads\Selenium Easy - Ajax Form submit demo for automation_but.html")
send_input_id(name_element_id,'python')
send_input_id(comment_element_id,'python is programming language')
driver.find_element_by_id(submit_button_element_id).click()
output = driver.find_element_by_id(submitted_text_element_id).text
print(output)
"""
driver = visit(r"C:\Users\niran\Downloads\Ajax.html")
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/button').click()
output = driver.find_element_by_id('div5').text
if output == 'fifth':
    assert True
else:
    assert False
#element = WebDriverWait(driver, 2)
#print(element.until(EC.text_to_be_present_in_element((By.ID, 'div5'),'fifth')))

driver.close()