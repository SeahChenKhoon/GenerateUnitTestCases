import pytest
from src.factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive_integer():
    assert factorial(5) == 120

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_negative_raises_value_error():
    with pytest.raises(ValueError) as exc_info:
        factorial(-1)
    assert str(exc_info.value) == "Factorial is not defined for negative integers."