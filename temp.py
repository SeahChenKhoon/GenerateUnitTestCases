import pytest
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference

def test_circle_area_positive_radius():
    radius = 5.0
    expected_area = math.pi * radius ** 2
    assert circle_area(radius) == pytest.approx(expected_area)
