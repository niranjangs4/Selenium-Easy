from Locators.elements import *
from libs_utils.web_launch import *

driver = visit(r'https://www.seleniumeasy.com/test/table-pagination-demo.html')


def cell_verify():
    cell_count = 0
    rows = 0
    for _ in driver.find_elements_by_tag_name('tr'):
        for i in _.find_elements_by_tag_name('td'):
            if i.text == 'Table cell':
                cell_count += 1
            else:
                val = i.text
                if val:
                    ev = eval(val)
                    if isinstance(ev, int):
                        rows += 1
    if rows * 6 == cell_count:
        print('matching no of cells {}'.format(cell_count))
    else:
        print('not matching no of cells {} != {}'.format(cell_count,rows * 7))


cell_verify()
driver.find_element_by_xpath('//*[@id="myPager"]/li[3]/a').click()
cell_verify()
driver.find_element_by_xpath('//*[@id="myPager"]/li[4]/a').click()
cell_verify()
time.sleep(5)
driver.close()
