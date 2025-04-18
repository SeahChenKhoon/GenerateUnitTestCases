import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest

def test_circle_area_with_positive_radius():
    # Arrange
    radius = 5.0
    expected_area = math.pi * radius ** 2

def test_circle_area_with_zero_radius():
    # Arrange
    radius = 0.0
    expected_area = 0.0

def test_circle_area_with_negative_radius_raises_value_error():
    # Arrange
    radius = -5.0

def test_circle_circumference_with_positive_radius():
    # Arrange
    radius = 5.0
    expected_circumference = 2 * math.pi * radius

def test_circle_circumference_with_zero_radius():
    # Arrange
    radius = 0.0
    expected_circumference = 0.0

def test_circle_circumference_with_negative_radius_raises_value_error():
    # Arrange
    radius = -5.0