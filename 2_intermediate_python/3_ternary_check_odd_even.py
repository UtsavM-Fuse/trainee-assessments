"""
Odd-Even Check Module

This module provides a function to check if a given integer is odd or even using a ternary operator.
"""


def check_odd_even(number: int) -> str:
    """
    Check if the given number is odd or even using a ternary operator.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    Examples:
        >>> check_odd_even(10)
        'Even'
        >>> check_odd_even(7)
        'Odd'
        >>> check_odd_even(0)
        'Even'
    """
    return "Even" if number % 2 == 0 else "Odd"


def test_check_odd_even():
    """
    This function is a test suite for the `check_odd_even` function
    """
    # Test case 1: Even number
    assert check_odd_even(10) == "Even"

    # Test case 2: Odd number
    assert check_odd_even(7) == "Odd"

    # Test case 3: Zero (Even)
    assert check_odd_even(0) == "Even"

    # Test case 4: Negative even number
    assert check_odd_even(-4) == "Even"

    # Test case 5: Negative odd number
    assert check_odd_even(-9) == "Odd"

    # Test case 6: Large even number
    assert check_odd_even(1000000) == "Even"

    # Test case 7: Large odd number
    assert check_odd_even(999999) == "Odd"


if __name__ == "__main__":
    test_check_odd_even()
    print("All test cases passed!")
