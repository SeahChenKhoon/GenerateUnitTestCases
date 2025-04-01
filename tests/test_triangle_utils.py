# No imports found in original file
from src.triangle_utils import triangle_perimeter, triangle_area
import pytest

def test_triangle_perimeter_positive_sides():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_with_zero_side():
    with pytest.raises(ValueError) as excinfo:
        triangle_perimeter(0, 4, 5)
    assert str(excinfo.value) == "All side lengths must be greater than zero."

def test_triangle_perimeter_with_negative_side():
    with pytest.raises(ValueError) as excinfo:
        triangle_perimeter(-1, 4, 5)
    assert str(excinfo.value) == "All side lengths must be greater than zero."

def test_triangle_area_positive_base_and_height():
    assert triangle_area(4, 5) == 10.0

def test_triangle_area_with_zero_base():
    with pytest.raises(ValueError) as excinfo:
        triangle_area(0, 5)
    assert str(excinfo.value) == "Base and height must be greater than zero."

def test_triangle_area_with_negative_height():
    with pytest.raises(ValueError) as excinfo:
        triangle_area(4, -1)
    assert str(excinfo.value) == "Base and height must be greater than zero."