import pytest
import math
from src.circle_utils import circle_area, circle_circumference

def test_circle_area_with_positive_radius():
    radius = 5
    expected_area = math.pi * radius ** 2
    assert circle_area(radius) == pytest.approx(expected_area)

def test_circle_area_with_zero_radius():
    assert circle_area(0) == 0

def test_circle_area_with_negative_radius_raises_value_error():
    with pytest.raises(ValueError):
        circle_area(-1)

def test_circle_circumference_with_positive_radius():
    radius = 5
    expected_circumference = 2 * math.pi * radius
    assert circle_circumference(radius) == pytest.approx(expected_circumference)

def test_circle_circumference_with_zero_radius():
    assert circle_circumference(0) == 0

def test_circle_circumference_with_negative_radius_raises_value_error():
    with pytest.raises(ValueError):
        circle_circumference(-1)