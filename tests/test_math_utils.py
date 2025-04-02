import pytest
# No imports found in original file
from src.math_utils import factorial, is_prime, is_odd

import pytest

def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_positive_integer():
    assert factorial(5) == 120

def test_factorial_raises_value_error_on_negative_input():
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime_with_prime_number():
    assert is_prime(29) is True

def test_is_prime_with_non_prime_number():
    assert is_prime(10) is False

def test_is_prime_with_negative_number():
    assert is_prime(-5) is False

def test_is_prime_with_zero():
    assert is_prime(0) is False

def test_is_prime_with_one():
    assert is_prime(1) is False

def test_is_odd_with_odd_number():
    assert is_odd(3) is True

def test_is_odd_with_even_number():
    assert is_odd(4) is False

def test_is_odd_with_negative_odd_number():
    assert is_odd(-3) is True

def test_is_odd_with_negative_even_number():
    assert is_odd(-2) is False

def test_is_odd_with_zero():
    assert is_odd(0) is False