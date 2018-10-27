import sys

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = visit(r'https://www.seleniumeasy.com/test/bootstrap-download-progress-demo.html')
check_button = driver.find_element_by_id('cricle-btn').text
if 'Download' in check_button:
    progress = driver.find_element_by_class_name('percenttext').text
    assert '0%' == progress
    driver.find_element_by_id('cricle-btn').click()
    element = WebDriverWait(driver, 30)
    finish = element.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'percenttext'), '100%'))
    if finish:
        print('Download completed 100%')
driver.close()
