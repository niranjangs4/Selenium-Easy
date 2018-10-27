from libs_utils.web_launch import *
import time

driver = visit(r'https://www.seleniumeasy.com/test/jquery-date-picker-demo.html')

driver.find_element_by_xpath('//*[@id="from"]').click()
opt = Select(driver.find_element_by_class_name('ui-datepicker-month'))
opt.select_by_visible_text('Feb')
driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[5]/a').click()
time.sleep(5)


driver.find_element_by_xpath('//*[@id="to"]').click()
opt = Select(driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select'))
opt.select_by_visible_text('Sep')
driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()

time.sleep(5)
driver.close()
