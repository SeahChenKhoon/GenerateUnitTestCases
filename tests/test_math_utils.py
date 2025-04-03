import pytest
from theory_evaluation.math_utils import is_odd

def test_is_odd_with_odd_number():
    assert is_odd(3) is True

def test_is_odd_with_even_number():
    assert is_odd(4) is False

def test_is_odd_with_zero():
    assert is_odd(0) is False

def test_is_odd_with_negative_odd_number():
    assert is_odd(-5) is True

def test_is_odd_with_negative_even_number():
    assert is_odd(-6) is False