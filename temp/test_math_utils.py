import pytest
from theory_evaluation.math_utils import factorial, is_odd, is_prime

def test_factorial_positive_integer():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_negative_integer():
    with pytest.raises(ValueError, match="Factorial is not defined for negative integers."):
        factorial(-1)

def test_is_prime_prime_number():
    assert is_prime(7) is True

def test_is_prime_non_prime_number():
    assert is_prime(4) is False

def test_is_prime_one():
    assert is_prime(1) is False

def test_is_prime_zero():
    assert is_prime(0) is False

def test_is_prime_negative_number():
    assert is_prime(-5) is False

def test_is_odd_odd_number():
    assert is_odd(3) is True

def test_is_odd_even_number():
    assert is_odd(4) is False

def test_is_odd_zero():
    assert is_odd(0) is False