import pytest
from src.fizzbuzz import fizzbuzz

def test_fizzbuzz_returns_fizz_for_multiples_of_three():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(6) == "fizz"
    assert fizzbuzz(9) == "fizz"

def test_fizzbuzz_returns_buzz_for_multiples_of_five():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(20) == "buzz"

def test_fizzbuzz_returns_fizzbuzz_for_multiples_of_fifteen():
    assert fizzbuzz(15) == "fizz buzz"
    assert fizzbuzz(30) == "fizz buzz"
    assert fizzbuzz(45) == "fizz buzz"

def test_fizzbuzz_returns_number_for_non_multiples_of_three_five_or_fifteen():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(4) == 4
    assert fizzbuzz(7) == 7
    assert fizzbuzz(8) == 8
    assert fizzbuzz(11) == 11
    assert fizzbuzz(13) == 13
    assert fizzbuzz(14) == 14
    assert fizzbuzz(16) == 16
    assert fizzbuzz(17) == 17
    assert fizzbuzz(19) == 19