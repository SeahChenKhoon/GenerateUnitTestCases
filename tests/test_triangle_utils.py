# No imports found in original file
from src.triangle_utils import triangle_perimeter, triangle_area
import pytest

def test_triangle_perimeter_with_positive_sides():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_with_zero_side_raises_value_error():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 4, 5)

def test_triangle_perimeter_with_negative_side_raises_value_error():
    with pytest.raises(ValueError):
        triangle_perimeter(-1, 4, 5)

def test_triangle_perimeter_with_all_sides_zero_raises_value_error():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 0, 0)

def test_triangle_area_with_positive_base_and_height():
    assert triangle_area(4, 5) == 10.0

def test_triangle_area_with_zero_base_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(0, 5)

def test_triangle_area_with_negative_height_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(4, -5)

def test_triangle_area_with_zero_base_and_height_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(0, 0)