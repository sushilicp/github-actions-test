from calculator.operations import add
"""
Unit tests for calculator operations.
This module contains test cases for the following functions from the
calculator.operations module:
- add: Tests addition of two numbers.
- subtract: Tests subtraction of two numbers.
- multiple: Tests multiplication of two numbers.
Each test function asserts the correctness of its respective operation.
"""
from calculator.operations import subtract
from calculator.operations import multiple
from calculator.operations import divide


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(4, 5) == -1


def test_multiple():
    assert multiple(4, 5) == 20


def test_divide():
    assert divide(4, 2) == 2
