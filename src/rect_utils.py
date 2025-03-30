def rect_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    Returns:
        float: The area of the rectangle.
    """
    return length * width


def rect_perimeter(length: float, width: float) -> float:
    """
    Calculates the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    return 2 * (length + width)