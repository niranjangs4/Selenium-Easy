import sys
sys.path.append(r"H:\seleniumeasy")
from POM.drop_down import *


def test_single_select():
    assert single_select()


def test_multi_select():
    assert multi_select()
