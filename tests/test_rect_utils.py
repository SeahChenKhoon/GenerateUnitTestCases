import pytest
# No imports found in original file
from src.rect_utils import rect_area, rect_perimeter

import pytest

def test_rect_area_with_positive_values():
    assert rect_area(5, 4) == 20

def test_rect_area_with_zero_length():
    assert rect_area(0, 5) == 0

def test_rect_area_with_zero_width():
    assert rect_area(5, 0) == 0

def test_rect_area_with_zero_length_and_width():
    assert rect_area(0, 0) == 0

def test_rect_perimeter_with_positive_values():
    assert rect_perimeter(5, 4) == 18

def test_rect_perimeter_with_zero_length():
    assert rect_perimeter(0, 5) == 10

def test_rect_perimeter_with_zero_width():
    assert rect_perimeter(5, 0) == 10

def test_rect_perimeter_with_zero_length_and_width():
    assert rect_perimeter(0, 0) == 0