import pytest
from sample_package.calculator import add, divide, Calculator

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_multiply_default_precision():
    calc = Calculator()
    assert calc.multiply(2.1234, 2) == 4.25

def test_multiply_custom_precision():
    calc = Calculator(precision=4)
    assert calc.multiply(2.1234, 2) == 4.2468

def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8
