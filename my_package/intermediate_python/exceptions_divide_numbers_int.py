def divide_numbers(num1: int, num2: int) -> float:
    """
    Perform division of two integers and handle ValueError and ZeroDivisionError.

    Args:
        num1 (int): The numerator.
        num2 (int): The denominator.

    Returns:
        float: The result of division (num1 / num2).

    Raises:
        ValueError: If either num1 or num2 is not an integer.
        ZeroDivisionError: If the denominator (num2) is zero.

    Examples:
        >>> divide_numbers(10, 2)
        5.0

        >>> divide_numbers(8, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: Division by zero is not allowed. Please provide a non-zero denominator.

        >>> divide_numbers(5, "abc")
        Traceback (most recent call last):
        ...
        ValueError: Invalid input. Please enter valid integers for both numerator and denominator.
    """
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError(
            "Invalid input. Please enter valid integers for both numerator and denominator."
        )

    if num2 == 0:
        raise ZeroDivisionError(
            "Division by zero is not allowed. Please provide a non-zero denominator."
        )

    return num1 / num2


if __name__ == "__main__":
    try:
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))

        result = divide_numbers(num1, num2)
        print(f"Result: {result}")

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
