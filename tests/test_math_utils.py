# No imports found in original file
from src.math_utils import factorial, is_prime

def test_factorial_of_zero():
    assert factorial(0) == 1

def test_factorial_of_one():
    assert factorial(1) == 1

def test_factorial_of_positive_integer():
    assert factorial(5) == 120

def test_factorial_raises_value_error_on_negative_input():
    import pytest
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime_with_negative_number():
    assert not is_prime(-1)

def test_is_prime_with_zero():
    assert not is_prime(0)

def test_is_prime_with_one():
    assert not is_prime(1)

def test_is_prime_with_two():
    assert is_prime(2)

def test_is_prime_with_three():
    assert is_prime(3)

def test_is_prime_with_four():
    assert not is_prime(4)

def test_is_prime_with_large_prime_number():
    assert is_prime(29)

def test_is_prime_with_large_non_prime_number():
    assert not is_prime(35)

def test_is_prime_with_very_large_prime():
    assert is_prime(7919)

def test_is_prime_with_very_large_non_prime():
    assert not is_prime(7920)