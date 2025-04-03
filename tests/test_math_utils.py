import pytest
from theory_evaluation.math_utils import factorial, is_prime, is_odd

def test_factorial_with_positive_integer():
    assert factorial(5) == 120

def test_factorial_with_zero():
    assert factorial(0) == 1

def test_factorial_with_negative_integer_raises_value_error():
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime_with_prime_number():
    assert is_prime(7) is True

def test_is_prime_with_non_prime_number():
    assert is_prime(4) is False

def test_is_prime_with_one():
    assert is_prime(1) is False

def test_is_prime_with_two():
    assert is_prime(2) is True

def test_is_prime_with_three():
    assert is_prime(3) is True

def test_is_odd_with_odd_number():
    assert is_odd(3) is True

def test_is_odd_with_even_number():
    assert is_odd(4) is False