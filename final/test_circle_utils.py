import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest

def test_circle_area_returns_correct_value_on_valid_input():
    # Arrange
    radius = 3.0
    expected_area = math.pi * radius ** 2

def test_circle_area_raises_value_error_on_negative_radius():
    # Arrange
    radius = -1.0

def test_circle_area_returns_zero_on_zero_radius():
    # Arrange
    radius = 0.0
    expected_area = 0.0

def test_circle_circumference_returns_correct_value_on_valid_input():
    # Arrange
    radius = 3.0
    expected_circumference = 2 * math.pi * radius

def test_circle_circumference_raises_value_error_on_negative_radius():
    # Arrange
    radius = -1.0

def test_circle_circumference_returns_zero_on_zero_radius():
    # Arrange
    radius = 0.0
    expected_circumference = 0.0