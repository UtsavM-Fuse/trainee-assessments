"""
Bigger Number Finder Module

This module provides a function to find the bigger number among three integers.
"""


def find_bigger_number(a: int, b: int, c: int) -> int | str:
    """
    Find the bigger number among the three integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        int | str: The larger number among a, b, and c. If all numbers are equal, returns "Equal."

    Examples:
        >>> find_bigger_number(5, 10, 7)
        10
        >>> find_bigger_number(3, 3, 3)
        'Equal'
        >>> find_bigger_number(-2, -5, -1)
        -1
        >>> find_bigger_number(30, 15, 30)
        30
    """
    output = "Equal" if a == b == c else a if a > b and a > c else b if b > c else c

    return output


def test_find_bigger_number():
    """
    This function is a test suite for the `find_bigger_number` function
    """
    # Test case 1: Larger number is the first integer
    assert find_bigger_number(5, 10, 7) == 10

    # Test case 2: All numbers are equal
    assert find_bigger_number(3, 3, 3) == "Equal"

    # Test case 3: Larger number is the second integer
    assert find_bigger_number(-2, -5, -1) == -1

    # Test case 4: Larger number is the third integer
    assert find_bigger_number(100, 200, 300) == 300

    # Test case 5: Two numbers are equal, larger number is the third integer
    assert find_bigger_number(10, 20, 20) == 20

    # Test case 6: Two numbers are equal, larger number is the first integer
    assert find_bigger_number(25, 25, 10) == 25

    # Test case 7: Two numbers are equal, larger number is the second integer
    assert find_bigger_number(30, 15, 30) == 30


if __name__ == "__main__":
    test_find_bigger_number()
    print("All test cases passed!")
