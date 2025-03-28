import pytest
from src.factorial import factorial

def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_one():
    assert factorial(1) == 1

def test_factorial_of_positive_integer():
    assert factorial(5) == 120

def test_factorial_of_another_positive_integer():
    assert factorial(3) == 6

def test_factorial_raises_value_error_on_negative_input():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_of_large_number():
    assert factorial(10) == 3628800