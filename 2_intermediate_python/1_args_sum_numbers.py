def sum_numbers(*args: int | float) -> int | float:
    """
    Calculate the sum of all the given numbers.

    Args:
        *args: Any number of positional arguments (int or float).

    Returns:
        The sum of all the numbers passed as arguments.

    Examples:
        >>> sum_numbers(1, 2, 3)
        6
        >>> sum_numbers(1.5, 2.5, 3.5)
        7.5
        >>> sum_numbers(10, 20, 30, 40, 50)
        150
        >>> sum_numbers()
        0
    """
    return sum(args)


def test_sum_numbers():
    # Test case 1: Basic sum with integers
    assert sum_numbers(1, 2, 3) == 6

    # Test case 2: Sum with floats
    assert sum_numbers(1.5, 2.5, 3.5) == 7.5

    # Test case 3: Sum with a mix of integers and floats
    assert sum_numbers(10, 20.5, 30, 40.5, 50) == 151.0

    # Test case 4: Sum with negative numbers
    assert sum_numbers(-1, -2, -3) == -6

    # Test case 5: Sum with a single number
    assert sum_numbers(100) == 100

    # Test case 6: Sum with an empty list of arguments
    assert sum_numbers() == 0

    # Test case 7: Sum with only float arguments
    assert sum_numbers(1.1, 2.2, 3.3) == 6.6

    # Test case 8: Sum with no arguments (should raise TypeError)
    assert sum_numbers() == 0


if __name__ == "__main__":
    test_sum_numbers()
    print("All test cases passed!")
