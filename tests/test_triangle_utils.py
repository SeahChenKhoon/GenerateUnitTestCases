import pytest
# No imports found in original file
from src.triangle_utils import triangle_perimeter, triangle_area

import pytest

def test_triangle_perimeter_positive_lengths():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_zero_length_side_raises_value_error():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 4, 5)

def test_triangle_perimeter_negative_length_side_raises_value_error():
    with pytest.raises(ValueError):
        triangle_perimeter(3, -4, 5)

def test_triangle_perimeter_all_sides_positive_but_one_zero_raises_value_error():
    with pytest.raises(ValueError):
        triangle_perimeter(3, 0, 5)

def test_triangle_area_positive_base_and_height():
    assert pytest.approx(triangle_area(6, 4)) == 12.0

def test_triangle_area_zero_base_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(0, 4)

def test_triangle_area_negative_height_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(6, -4)

def test_triangle_area_zero_height_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(6, 0)

def test_triangle_area_negative_base_raises_value_error():
    with pytest.raises(ValueError):
        triangle_area(-6, 4)