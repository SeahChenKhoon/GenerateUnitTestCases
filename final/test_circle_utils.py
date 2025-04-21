import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest

def test_circle_area_positive_radius():
    # Arrange
    radius = 5.0
    expected_area = math.pi * radius ** 2
    
    # Act
    result = circle_area(radius)
    
    # Assert
    assert result == expected_area, f"Expected {expected_area}, got {result}"

def test_circle_area_zero_radius():
    # Arrange
    radius = 0.0
    expected_area = 0.0

def test_circle_area_negative_radius():
    # Arrange
    radius = -5.0

def test_circle_area_none_radius():
    # Arrange
    radius = None

def test_circle_circumference_positive_radius():
    # Arrange
    radius = 5.0
    expected_circumference = 2 * math.pi * radius
    
    # Act
    actual_circumference = circle_circumference(radius)
    
    # Assert
    assert actual_circumference == expected_circumference

def test_circle_circumference_zero_radius():
    # Arrange
    radius = 0.0
    expected_circumference = 0.0

def test_circle_circumference_negative_radius():
    # Arrange
    radius = -5.0

def test_circle_circumference_none_radius():
    # Arrange
    radius = None