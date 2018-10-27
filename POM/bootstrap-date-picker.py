from Locators.elements import *
from libs_utils.web_launch import *
import time
from selenium.webdriver.common.keys import Keys
driver = visit(r'https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html')



#//*[@id="sandbox-container1"]/div/input
driver.find_element_by_xpath('//*[@id="sandbox-container1"]/div/input').send_keys('05/09/2018')
driver.find_element_by_xpath('//*[@id="sandbox-container1"]/div/input').send_keys(Keys.ENTER)
#driver.find_element_by_xpath('//*[@id="sandbox-container1"]/div/input').send_keys(Keys.RETURN)
#driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/thead/tr[2]/th[1]').click()
#driver.find_element_by_xpath('/html/body/div[3]/div[1]/table/tbody/tr[2]/td[3]').click()




driver.find_element_by_xpath('//*[@id="datepicker"]/input[1]').send_keys('04/07/2018')
#driver.find_element_by_xpath('//*[@id="datepicker"]/input[1]').send_keys(Keys.RETURN)



driver.find_element_by_xpath('//*[@id="datepicker"]/input[2]').send_keys('05/09/2018')
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div[1]').click()

time.sleep(5)
driver.close()
