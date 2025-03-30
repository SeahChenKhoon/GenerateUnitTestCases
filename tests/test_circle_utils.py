import math
import pytest
from src.circle_utils import area_circle, perimeter_circle

def test_area_circle_with_positive_radius():
    assert math.isclose(area_circle(5), 78.53981633974483, rel_tol=1e-9)

def test_area_circle_with_zero_radius():
    assert area_circle(0) == 0

def test_area_circle_with_negative_radius():
    assert math.isclose(area_circle(-3), 28.274333882308138, rel_tol=1e-9)

def test_perimeter_circle_with_positive_radius():
    assert math.isclose(perimeter_circle(7), 43.982297150257104, rel_tol=1e-9)

def test_perimeter_circle_with_zero_radius():
    assert perimeter_circle(0) == 0

def test_perimeter_circle_with_negative_radius():
    assert math.isclose(perimeter_circle(-4), 25.132741228718345, rel_tol=1e-9)