import pytest
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference

def test_circle_area_positive_radius():
    assert circle_area(1) == pytest.approx(math.pi)
    assert circle_area(2) == pytest.approx(4 * math.pi)
    assert circle_area(0) == pytest.approx(0)
