import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest

def test_circle_area_valid_radius():
    test_cases = [
        (1, math.pi),
        (0, 0),
        (2, 4 * math.pi),
        (3.5, 3.5 ** 2 * math.pi)
    ]
    
    for radius, expected_area in test_cases:
        result = circle_area(radius)
        assert result == expected_area

def test_circle_area_negative_radius():
    radius = -1
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_area(radius)

@pytest.mark.parametrize("radius, expected_circumference", [
    (1, 2 * math.pi),
    (0, 0),
    (2.5, 2 * math.pi * 2.5),
])
def test_circle_circumference_valid_radius(radius, expected_circumference):
    result = circle_circumference(radius)
    assert result == expected_circumference

def test_circle_circumference_negative_radius():
    radius = -1
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_circumference(radius)