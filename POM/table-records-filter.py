import sys

sys.path.append(r'H:\seleniumeasy')
from Locators.elements import *
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/table-records-filter-demo.html')
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[2]').click()
table_value('/html/body/div[2]/div/div[2]/section/div/div')

time.sleep(10)
driver.close()
