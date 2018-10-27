from Locators.elements import *
from libs_utils.web_launch import *
import time


def setup_module():
    global handle
    handle = visit(select_dropdown_demo)


def single_select():
    for week in week_list:
        option = select_drop_down_id(select_list_element_by_id, week)
        output = handle.find_element_by_class_name(select_value_read_element_class).text
        time.sleep(2)
        if option and week in output:
            screen_capture(week)
            print("{} in {}".format(week, output))
    screen_capture('selection')
    return True


def multi_select():
    for city in city_list:
        option = select_drop_down_id(multi_select_list_element_by_id, city)
        handle.find_element_by_id(button_first_selected_element_id).click()
        output = handle.find_element_by_class_name(output_read_text_element_class).text
        time.sleep(2)
        if option and city in output:
            print("{} in {}".format(city, output))
    handle.find_element_by_id(button_all_selected_element_id).click()
    output_all = handle.find_element_by_class_name(output_read_text_element_class).text
    screen_capture('Multiple selection')
    time.sleep(5)
    print(output_all)
    return True


def teardown_module():
    handle.close()
