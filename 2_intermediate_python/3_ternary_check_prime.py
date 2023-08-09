"""
Prime Check Module

This module provides a function to check if a given positive integer 
is prime using a ternary operator.
"""


def check_prime(num: int) -> str:
    """
    Check if the given number is prime using a ternary operator.

    Args:
        num (int): The positive integer to be checked.

    Returns:
        str: "Prime" if the number is prime, "Not Prime" otherwise.

    Examples:
        >>> check_prime(5)
        'Prime'
        >>> check_prime(10)
        'Not Prime'
        >>> check_prime(17)
        'Prime'
        >>> check_prime(1)
        'Not Prime'
    """

    output = (
        "Not Prime"
        if num < 2
        else "Prime"
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        else "Not Prime"
    )
    return output


def test_check_prime():
    """
    This function is a test suite for the `check_prime` function
    """
    # Test case 1: Prime number (5)
    assert check_prime(5) == "Prime"

    # Test case 2: Not Prime (10)
    assert check_prime(10) == "Not Prime"

    # Test case 3: Prime number (17)
    assert check_prime(17) == "Prime"

    # Test case 4: Not Prime (1)
    assert check_prime(1) == "Not Prime"

    # Test case 5: Prime number (2)
    assert check_prime(2) == "Prime"

    # Test case 6: Not Prime (0)
    assert check_prime(0) == "Not Prime"

    # Test case 7: Not Prime (Negative number)
    assert check_prime(-7) == "Not Prime"

    # Test case 8: Prime number (Large prime)
    assert check_prime(997) == "Prime"

    # Test case 9: Not Prime (Large non-prime)
    assert check_prime(1000) == "Not Prime"


if __name__ == "__main__":
    test_check_prime()
    print("All test cases passed!")
