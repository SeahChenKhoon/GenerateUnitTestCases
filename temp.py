import pytest
import math
from theory_evaluation.circle_utils import circle_area, circle_circumference

def test_circle_circumference_negative_radius():
    radius = -5
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_circumference(radius)
