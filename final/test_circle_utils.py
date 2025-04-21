from theory_evaluation.circle_utils import circle_area, circle_circumference
import math
import pytest

def test_circle_area_positive_radius():
    radius = 5.0
    expected_area = math.pi * radius ** 2
    result = circle_area(radius)
    assert result == expected_area

def test_circle_area_zero_radius():
    radius = 0.0
    expected_area = 0.0
    result = circle_area(radius)
    assert result == expected_area

def test_circle_area_negative_radius():
    radius = -5.0
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_area(radius)

def test_circle_area_none_radius():
    radius = None
    with pytest.raises(TypeError):
        circle_area(radius)

def test_circle_circumference_positive_radius():
    radius = 5.0
    expected_circumference = 2 * math.pi * radius
    result = circle_circumference(radius)
    assert result == expected_circumference

def test_circle_circumference_zero_radius():
    radius = 0.0
    expected_circumference = 0.0
    result = circle_circumference(radius)
    assert result == expected_circumference

def test_circle_circumference_negative_radius():
    radius = -5.0
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_circumference(radius)

def test_circle_circumference_none_radius():
    radius = None
    with pytest.raises(TypeError):
        circle_circumference(radius)