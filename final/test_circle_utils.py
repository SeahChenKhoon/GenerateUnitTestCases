import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


import math
from theory_evaluation.circle_utils import circle_area, circle_circumference
import pytest


def test_circle_area_positive_radius():
    radius = 5
    expected_area = math.pi * radius ** 2
    assert circle_area(radius) == pytest.approx(expected_area)

def test_circle_area_zero_radius():
    radius = 0
    expected_area = 0
    assert circle_area(radius) == pytest.approx(expected_area)

def test_circle_area_negative_radius():
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_area(-1)

def test_circle_circumference_positive_radius():
    radius = 5
    expected_circumference = 2 * math.pi * radius
    assert circle_circumference(radius) == pytest.approx(expected_circumference)

def test_circle_circumference_zero_radius():
    radius = 0
    expected_circumference = 0
    assert circle_circumference(radius) == pytest.approx(expected_circumference)

def test_circle_circumference_negative_radius():
    with pytest.raises(ValueError, match="Radius cannot be negative."):
        circle_circumference(-1)
