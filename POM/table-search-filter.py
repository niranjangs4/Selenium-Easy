import sys

sys.path.append(r'H:\seleniumeasy')
from Locators.elements import *
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/table-search-filter-demo.html')
"""
table_value('//*[@id="task-table"]')

driver.find_element_by_xpath('//*[@id="task-table-filter"]').send_keys('progress')
print("*************** Filter ******************")

table_value('//*[@id="task-table"]')
"""
print("*************** 2nd Filter ******************")
table_value('/html/body/div[2]/div/div[2]/div[2]/div')

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input').send_keys('Brigade')
print("Filtred")
table_value('/html/body/div[2]/div/div[2]/div[2]/div')

time.sleep(5)
driver.close()
