import math


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


def circle_circumference(radius: float) -> float:
    """
    Calculate the circumference of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Circumference of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * math.pi * radius
