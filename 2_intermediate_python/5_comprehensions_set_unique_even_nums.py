"""
Module: unique_even_numbers

This module provides a function to create a set containing unique even numbers from a given list.
"""


def unique_even_numbers(numbers: list[int]) -> set[int]:
    """
    Create a set containing unique even numbers from the given list.

    Args:
        numbers (list[int]): The list of numbers.

    Returns:
        set[int]: A set containing unique even numbers.

    Examples:
        >>> numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> unique_even_numbers(numbers1)
        {2, 4, 6, 8}

        >>> numbers2 = [10, 11, 12, 13, 14, 15]
        >>> unique_even_numbers(numbers2)
        {10, 12, 14}
    """
    return {num for num in numbers if num % 2 == 0}


def test_unique_even_numbers():
    """
    This function is a test suite for the `unique_even_numbers` function
    """
    # Test case 1: Normal case with mixed numbers
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert unique_even_numbers(numbers1) == {2, 4, 6, 8}

    # Test case 2: Normal case with all even numbers
    numbers2 = [10, 12, 14, 16, 18, 20]
    assert unique_even_numbers(numbers2) == {10, 12, 14, 16, 18, 20}

    # Test case 3: Normal case with all odd numbers (should return an empty set)
    numbers3 = [1, 3, 5, 7, 9]
    assert unique_even_numbers(numbers3) == set()

    # Test case 4: Empty list (should return an empty set)
    numbers4 = []
    assert unique_even_numbers(numbers4) == set()

    # Test case 5: List with negative numbers
    numbers5 = [-2, 0, 2, 4, -6, -8]
    assert unique_even_numbers(numbers5) == {-8, -6, -2, 0, 2, 4}

    # Test case 6: List with floating-point numbers (should ignore the non-integer elements)
    numbers6 = [2.5, 3.5, 4.0, 5.5, 6.0]
    assert unique_even_numbers(numbers6) == {4.0, 6.0}

    # Test case 7: List with duplicate even numbers
    numbers7 = [2, 4, 6, 2, 4, 8, 6, 10]
    assert unique_even_numbers(numbers7) == {2, 4, 6, 8, 10}


if __name__ == "__main__":
    test_unique_even_numbers()
    print("All test cases passed!")
