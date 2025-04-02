import pytest
from src.triangle_utils import triangle_perimeter, triangle_area

def test_triangle_perimeter_valid_sides():
    assert triangle_perimeter(3, 4, 5) == 12

def test_triangle_perimeter_zero_side():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 4, 5)

def test_triangle_perimeter_negative_side():
    with pytest.raises(ValueError):
        triangle_perimeter(3, -4, 5)

def test_triangle_perimeter_all_zero_sides():
    with pytest.raises(ValueError):
        triangle_perimeter(0, 0, 0)

def test_triangle_perimeter_all_negative_sides():
    with pytest.raises(ValueError):
        triangle_perimeter(-1, -1, -1)

def test_triangle_area_valid_dimensions():
    assert pytest.approx(triangle_area(6, 4)) == 12.0

def test_triangle_area_zero_base():
    with pytest.raises(ValueError):
        triangle_area(0, 5)

def test_triangle_area_negative_height():
    with pytest.raises(ValueError):
        triangle_area(4, -5)

def test_triangle_area_zero_height():
    with pytest.raises(ValueError):
        triangle_area(5, 0)

def test_triangle_area_negative_base():
    with pytest.raises(ValueError):
        triangle_area(-5, 4)

def test_triangle_area_zero_base_and_height():
    with pytest.raises(ValueError):
        triangle_area(0, 0)

def test_triangle_area_negative_base_and_height():
    with pytest.raises(ValueError):
        triangle_area(-5, -5)