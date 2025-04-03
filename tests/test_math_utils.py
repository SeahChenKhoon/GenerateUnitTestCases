import pytest
from theory_evaluation.math_utils import factorial, is_prime, is_odd

def test_factorial_positive_integers():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_negative_integer():
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime_for_non_primes():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(9)
    assert not is_prime(100)

def test_is_prime_for_primes():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)

def test_is_odd_for_even_numbers():
    assert not is_odd(0)
    assert not is_odd(2)
    assert not is_odd(4)
    assert not is_odd(100)

def test_is_odd_for_odd_numbers():
    assert is_odd(1)
    assert is_odd(3)
    assert is_odd(5)
    assert is_odd(101)