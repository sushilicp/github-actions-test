from calculator.operations import add
from calculator.operations import subtract
from calculator.operations import multiple


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(4, 5) == -1


def test_multiple():
    assert multiple(4, 5) == 20
