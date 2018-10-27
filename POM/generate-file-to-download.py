import sys
import os

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/generate-file-to-download-demo.html')
driver.find_element_by_id('textbox').send_keys('python.org')
driver.find_element_by_id('create').click()
filename = r'C:\Users\Niranjan Kumar G S\Downloads\easyinfo.txt'
if os.path.exists(filename):
    os.remove(filename)
driver.find_element_by_id('link-to-download').click()
time.sleep(6)
if os.path.exists(filename):
    with open(filename) as data:
        print('file downloaded')
        print(data.read())
else:
    print('file not found')
driver.close()
