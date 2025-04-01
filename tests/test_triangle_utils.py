# No imports found in original file
from src.triangle_utils import triangle_perimeter
import pytest

def test_triangle_perimeter_with_positive_sides():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_with_large_values():
    assert triangle_perimeter(100, 200, 300) == 600

def test_triangle_perimeter_with_float_values():
    assert triangle_perimeter(3.5, 4.5, 5.5) == 13.5

def test_triangle_perimeter_raises_error_on_negative_side():
    with pytest.raises(ValueError):
        triangle_perimeter(-1, 2, 3)

def test_triangle_perimeter_raises_error_on_zero_length_side():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 5, 5)

def test_triangle_perimeter_raises_error_on_all_sides_non_positive():
    with pytest.raises(ValueError):
        triangle_perimeter(-1, -1, -1)

def test_triangle_perimeter_raises_error_on_one_side_zero_others_negative():
    with pytest.raises(ValueError):
        triangle_perimeter(0, -2, -3)