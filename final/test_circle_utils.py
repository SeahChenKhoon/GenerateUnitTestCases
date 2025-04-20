import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest

def test_circle_area_positive_radius():
    # Arrange
    radius = 5
    expected_area = math.pi * radius ** 2

def test_circle_area_zero_radius():
    # Arrange
    radius = 0
    expected_area = 0

def test_circle_area_negative_radius():
    # Arrange
    radius = -5

def test_circle_circumference_positive_radius():
    # Arrange
    radius = 5
    expected_circumference = 2 * math.pi * radius

def test_circle_circumference_zero_radius():
    # Arrange
    radius = 0
    expected_circumference = 0

def test_circle_circumference_negative_radius():
    # Arrange
    radius = -5