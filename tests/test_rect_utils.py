import pytest
from src.rect_utils import rect_area, rect_perimeter

def test_rect_area_with_positive_values():
    assert rect_area(5, 10) == 50

def test_rect_area_with_zero_length():
    assert rect_area(0, 10) == 0

def test_rect_area_with_zero_width():
    assert rect_area(10, 0) == 0

def test_rect_area_with_zero_length_and_width():
    assert rect_area(0, 0) == 0

def test_rect_perimeter_with_positive_values():
    assert rect_perimeter(5, 10) == 30

def test_rect_perimeter_with_zero_length():
    assert rect_perimeter(0, 10) == 20

def test_rect_perimeter_with_zero_width():
    assert rect_perimeter(10, 0) == 20

def test_rect_perimeter_with_zero_length_and_width():
    assert rect_perimeter(0, 0) == 0