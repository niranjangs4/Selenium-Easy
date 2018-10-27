import sys

sys.path.append(r"H:\seleniumeasy")
from POM.input_form import *


def test_single_check_box():
    assert single_checkbox()


def test_multiple_check_box():
    assert multiple_checkbox()

    