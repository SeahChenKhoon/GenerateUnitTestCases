def triangle_perimeter(a: float, b: float, c: float) -> float:
    """
    Calculate the perimeter of a triangle.

    Args:
        a (float): Length of side A.
        b (float): Length of side B.
        c (float): Length of side C.

    Returns:
        float: The perimeter of the triangle.

    Raises:
        ValueError: If any side length is non-positive.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All side lengths must be greater than zero.")
    
    return a + b + c