import pytest
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference

def test_circle_area_with_positive_radius():
    assert circle_area(1) == pytest.approx(math.pi)
    assert circle_area(2) == pytest.approx(4 * math.pi)
    assert circle_area(0.5) == pytest.approx(0.25 * math.pi)

def test_circle_area_with_zero_radius():
    assert circle_area(0) == pytest.approx(0)

def test_circle_area_with_negative_radius():
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_area(-1)

def test_circle_circumference_with_positive_radius():
    assert circle_circumference(1) == pytest.approx(2 * math.pi)
    assert circle_circumference(2) == pytest.approx(4 * math.pi)
    assert circle_circumference(0.5) == pytest.approx(math.pi)

def test_circle_circumference_with_zero_radius():
    assert circle_circumference(0) == pytest.approx(0)

def test_circle_circumference_with_negative_radius():
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_circumference(-1)