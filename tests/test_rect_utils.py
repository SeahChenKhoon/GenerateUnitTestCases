# No imports found in original file
from src.rect_utils import rect_area, rect_perimeter

def test_rect_area_with_positive_numbers():
    assert rect_area(5, 3) == 15

def test_rect_area_with_zero():
    assert rect_area(0, 5) == 0
    assert rect_area(5, 0) == 0
    assert rect_area(0, 0) == 0

def test_rect_area_with_negative_numbers():
    assert rect_area(-5, 3) == -15
    assert rect_area(5, -3) == -15
    assert rect_area(-5, -3) == 15

def test_rect_perimeter_with_positive_numbers():
    assert rect_perimeter(5, 3) == 16

def test_rect_perimeter_with_zero():
    assert rect_perimeter(0, 5) == 10
    assert rect_perimeter(5, 0) == 10
    assert rect_perimeter(0, 0) == 0

def test_rect_perimeter_with_negative_numbers():
    assert rect_perimeter(-5, 3) == -4
    assert rect_perimeter(5, -3) == 4
    assert rect_perimeter(-5, -3) == -16