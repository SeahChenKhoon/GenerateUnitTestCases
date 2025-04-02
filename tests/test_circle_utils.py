import pytest
from src.circle_utils import circle_area, circle_circumference

def test_circle_area_with_positive_radius():
    assert circle_area(5) == pytest.approx(78.53981633974483)

def test_circle_area_with_zero_radius():
    assert circle_area(0) == pytest.approx(0)

def test_circle_area_with_negative_radius():
    with pytest.raises(ValueError):
        circle_area(-1)

def test_circle_circumference_with_positive_radius():
    assert circle_circumference(5) == pytest.approx(31.41592653589793)

def test_circle_circumference_with_zero_radius():
    assert circle_circumference(0) == pytest.approx(0)

def test_circle_circumference_with_negative_radius():
    with pytest.raises(ValueError):
        circle_circumference(-1)