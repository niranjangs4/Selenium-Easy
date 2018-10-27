import sys
import re
from selenium.webdriver.common.keys import Keys

sys.path.append(r'H:\seleniumeasy')
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/drag-drop-range-sliders-demo.html')


def drag_slider(element):
    for i in element:
        check_button = driver.find_element_by_id('slider{}'.format(i))
        h1_text = check_button.find_element_by_tag_name('h4').text
        default_value = int(re.search(r'\d+', h1_text).group())
        actual_value = int(check_button.find_element_by_tag_name('output').text)
        assert default_value == actual_value
        increment = actual_value + 30

        while increment >= actual_value:
            check_button.find_element_by_tag_name('input').send_keys(Keys.ARROW_RIGHT)
            actual_value = int(check_button.find_element_by_tag_name('output').text)
        print(actual_value, increment)



drag_slider([1, 2, 3, 4, 5, 6])
time.sleep(10)
driver.close()
