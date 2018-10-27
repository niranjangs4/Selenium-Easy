from Locators.elements import *
from libs_utils.web_launch import *
import time

from libs_utils.config import readconfig


def setup_module():
    global handle
    handle = visit(simple_form_demo)


def single_input():
    value = readconfig('INPUTS', 'name')
    if send_input_id(single_input_field_element_id, value):
        handle.find_element_by_css_selector(single_input_button_element_css).click()
    output = handle.find_element_by_id(single_output_element_id).text
    screen_capture('single_input')
    print("{} == {}".format(value, output))
    time.sleep(4)
    return value == output


def two_input():
    num1 = readconfig('INPUTS', 'num1')
    num2 = readconfig('INPUTS', 'num2')
    if send_input_id(two_input_a_element_id, num1):
        assert True
    if send_input_id(two_input_b_element_id, num2):
        assert True
    handle.find_element_by_css_selector(click_output_button_element_css).click()
    screen_capture('two_input')
    output = handle.find_element_by_id(total_output_element_id).text
    time.sleep(4)
    return int(num1) + int(num2) == int(output)


def teardown_module():
    handle.close()
