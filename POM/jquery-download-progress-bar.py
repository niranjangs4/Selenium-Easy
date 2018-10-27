import sys

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = visit(r'https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')
check_button = driver.find_element_by_id('downloadButton').text
if check_button == 'Start Download':
    driver.find_element_by_id('downloadButton').click()
    time.sleep(100)
    element = WebDriverWait(driver, 100)
    finish = element.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'progress-label'), 'Complete!'))
    print(finish)
    if finish:
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button').click()
time.sleep(10)

driver.close()
