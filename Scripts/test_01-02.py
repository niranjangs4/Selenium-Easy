import sys
sys.path.append(r"H:\seleniumeasy")
from POM.simple_form import *


def test_single_input():
    assert single_input()


def test_two_input():
    assert two_input()
