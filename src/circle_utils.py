import math

def area_circle(radius: float) -> float:
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2


def perimeter_circle(radius: float) -> float:
    """
    Calculates the perimeter (circumference) of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The perimeter of the circle.
    """
    return 2 * math.pi * radius