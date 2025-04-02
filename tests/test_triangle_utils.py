import pytest
from src.triangle_utils import triangle_perimeter, triangle_area

def test_triangle_perimeter_with_valid_sides():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_with_zero_side():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 4, 5)

def test_triangle_perimeter_with_negative_side():
    with pytest.raises(ValueError):
        triangle_perimeter(3, -4, 5)

def test_triangle_perimeter_with_all_negative_sides():
    with pytest.raises(ValueError):
        triangle_perimeter(-3, -4, -5)

def test_triangle_area_with_valid_dimensions():
    assert pytest.approx(triangle_area(6, 4)) == 12.0

def test_triangle_area_with_zero_base():
    with pytest.raises(ValueError):
        triangle_area(0, 4)

def test_triangle_area_with_negative_height():
    with pytest.raises(ValueError):
        triangle_area(6, -4)

def test_triangle_area_with_zero_base_and_height():
    with pytest.raises(ValueError):
        triangle_area(0, 0)