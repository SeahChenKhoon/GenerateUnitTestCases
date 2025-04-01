# No imports found in original file
from src.triangle_utils import triangle_perimeter
import pytest

def test_triangle_perimeter_with_positive_sides():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_with_float_sides():
    assert triangle_perimeter(3.5, 4.2, 5.3) == 13.0

def test_triangle_perimeter_raises_error_on_zero_side():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 4, 5)

def test_triangle_perimeter_raises_error_on_negative_side():
    with pytest.raises(ValueError):
        triangle_perimeter(3, -4, 5)

def test_triangle_perimeter_raises_error_on_all_sides_non_positive():
    with pytest.raises(ValueError):
        triangle_perimeter(-1, -1, -1)