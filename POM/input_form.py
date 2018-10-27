import sys
sys.path.append(r"H:\seleniumeasy")
from Locators.elements import *
from libs_utils.web_launch import visit,screen_capture
import time


def setup_module():
    global handle
    handle = visit(checkbox_demo)


def single_checkbox():
    handle.find_element_by_id(single_check_element_id).click()
    time.sleep(1)
    screen_capture('Single_click')
    return True


def multiple_checkbox():
    elem = handle.find_elements_by_class_name(multiple_check_elements_class)
    for item in elem:
        item.click()
        time.sleep(.5)
    screen_capture('Multiple_click')
    return True


def teardown_module():
    handle.close()
