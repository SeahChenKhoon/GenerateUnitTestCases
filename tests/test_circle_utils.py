import pytest
import math
from src.circle_utils import circle_area, circle_circumference

def test_circle_area_with_positive_radius():
    assert pytest.approx(circle_area(5), 0.01) == math.pi * 25

def test_circle_area_with_zero_radius():
    assert circle_area(0) == 0

def test_circle_area_with_negative_radius_raises_exception():
    with pytest.raises(ValueError) as excinfo:
        circle_area(-1)
    assert str(excinfo.value) == "Radius cannot be negative."

def test_circle_circumference_with_positive_radius():
    assert pytest.approx(circle_circumference(5), 0.01) == 2 * math.pi * 5

def test_circle_circumference_with_zero_radius():
    assert circle_circumference(0) == 0

def test_circle_circumference_with_negative_radius_raises_exception():
    with pytest.raises(ValueError) as excinfo:
        circle_circumference(-1)
    assert str(excinfo.value) == "Radius cannot be negative."