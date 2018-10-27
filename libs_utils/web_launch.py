from selenium import webdriver
from .config import readconfig
from selenium.webdriver.support.select import Select
import time


def visit(link):
    global driver
    selection = readconfig('WEB', 'Browser')
    if selection.lower() == 'edge':
        driver = webdriver.Edge()
    elif selection.lower() == 'ie':
        driver = webdriver.Ie()
    elif selection.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get(link)
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver


def screen_capture(name):
    time_str = time.strftime("%Y%m%d-%H%M%S")
    driver.save_screenshot(r"H:\seleniumeasy\screenshots\{}_{}.png".format(name, time_str))
    return True


def send_input_id(elem, value):
    driver.find_element_by_id(elem).clear()
    driver.find_element_by_id(elem).send_keys(value)
    return True


def select_drop_down_id(elem, value):
    option = Select(driver.find_element_by_id(elem))
    option.select_by_visible_text(value)
    return True


def table_value(element):
    count = 0
    for val in driver.find_elements_by_xpath(element):
        for _ in val.find_elements_by_tag_name('tr'):
            for i in _.find_elements_by_tag_name('td'):
                if 'No result' in i.text:
                    print('Given data is not avalible')
                elif i.text:
                    print(i.text)
                    count += 1
    print(count)
