import pytest
import math
from src.circle_utils import area_circle, perimeter_circle

def test_area_circle_with_positive_radius():
    radius = 5
    expected_area = math.pi * radius ** 2
    assert area_circle(radius) == expected_area

def test_area_circle_with_zero_radius():
    radius = 0
    expected_area = 0
    assert area_circle(radius) == expected_area

def test_area_circle_with_negative_radius():
    radius = -5
    expected_area = math.pi * radius ** 2
    assert area_circle(radius) == expected_area

def test_perimeter_circle_with_positive_radius():
    radius = 5
    expected_perimeter = 2 * math.pi * radius
    assert perimeter_circle(radius) == expected_perimeter

def test_perimeter_circle_with_zero_radius():
    radius = 0
    expected_perimeter = 0
    assert perimeter_circle(radius) == expected_perimeter

def test_perimeter_circle_with_negative_radius():
    radius = -5
    expected_perimeter = 2 * math.pi * radius
    assert perimeter_circle(radius) == expected_perimeter

def test_area_circle_with_large_radius():
    radius = 1e6
    expected_area = math.pi * radius ** 2
    assert area_circle(radius) == expected_area

def test_perimeter_circle_with_large_radius():
    radius = 1e6
    expected_perimeter = 2 * math.pi * radius
    assert perimeter_circle(radius) == expected_perimeter

def test_area_circle_with_very_small_radius():
    radius = 1e-6
    expected_area = math.pi * radius ** 2
    assert area_circle(radius) == expected_area

def test_perimeter_circle_with_very_small_radius():
    radius = 1e-6
    expected_perimeter = 2 * math.pi * radius
    assert perimeter_circle(radius) == expected_perimeter