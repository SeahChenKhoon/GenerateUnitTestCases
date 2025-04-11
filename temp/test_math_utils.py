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
        factorial(-5)

def test_is_prime_negative_integer():
    assert not is_prime(-5)

def test_is_prime_zero():
    assert not is_prime(0)

def test_is_prime_one():
    assert not is_prime(1)

def test_is_prime_two():
    assert is_prime(2)

def test_is_prime_three():
    assert is_prime(3)

def test_is_prime_four():
    assert not is_prime(4)

def test_is_prime_large_prime():
    assert is_prime(29)

def test_is_prime_large_non_prime():
    assert not is_prime(30)

def test_is_odd_even_number():
    assert not is_odd(4)

def test_is_odd_odd_number():
    assert is_odd(5)

def test_is_odd_zero():
    assert not is_odd(0)