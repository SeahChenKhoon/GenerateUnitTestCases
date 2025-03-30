def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """
    Determines whether a given integer is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True