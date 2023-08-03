from functools import reduce


def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given integer.

    Args:
        n (int): The integer for which to calculate the factorial.

    Returns:
        int: The factorial of the input integer.

    Raises:
        ValueError: If the input is negative.

    Examples:
        >>> calculate_factorial(5)
        120
        >>> calculate_factorial(0)
        1
        >>> calculate_factorial(10)
        3628800
        >>> calculate_factorial(-5)
        Traceback (most recent call last):
        ...
        ValueError: Factorial is not defined for negative numbers.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def test_calculate_factorial():
    # Test case 1: Factorial of 5
    assert calculate_factorial(5) == 120

    # Test case 2: Factorial of 0
    assert calculate_factorial(0) == 1

    # Test case 3: Factorial of 10
    assert calculate_factorial(10) == 3628800

    # Test case 4: Factorial of 1
    assert calculate_factorial(1) == 1

    # Test case 5: Factorial of a negative number (should raise ValueError)
    try:
        result5 = calculate_factorial(-5)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError but got no exception"


if __name__ == "__main__":
    test_calculate_factorial()
    print("All test cases passed!")
