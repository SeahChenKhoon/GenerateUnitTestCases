import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest

def test_circle_area_with_positive_radius():
    radius = 5.0
    expected_area = math.pi * radius ** 2
    result = circle_area(radius)
    assert result == expected_area

def test_circle_area_with_zero_radius():
    radius = 0.0
    expected_area = 0.0
    result = circle_area(radius)
    assert result == expected_area

def test_circle_area_with_negative_radius_raises_value_error():
    radius = -5.0
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_area(radius)

def test_circle_circumference_with_positive_radius():
    radius = 5.0
    expected_circumference = 2 * math.pi * radius
    result = circle_circumference(radius)
    assert result == expected_circumference

def test_circle_circumference_with_zero_radius():
    radius = 0.0
    expected_circumference = 0.0
    result = circle_circumference(radius)
    assert result == expected_circumference

def test_circle_circumference_with_negative_radius_raises_value_error():
    radius = -5.0
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_circumference(radius)