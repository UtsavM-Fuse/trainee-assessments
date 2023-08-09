"""
Module: convert_to_integer

This module provides a function to convert user input to an integer.
"""


def convert_to_integer(user_input: str) -> int:
    """
    Convert the given user input to an integer.

    Args:
        user_input (str): The user-provided input.

    Returns:
        int: The integer representation of the input.

    Raises:
        ValueError: If the input cannot be converted to an integer.

    Examples:
        >>> convert_to_integer("123")
        123

        >>> convert_to_integer("abc")
        Traceback (most recent call last):
        ...
        ValueError: Invalid input. Please enter a valid integer.
    """
    try:
        integer_value = int(user_input)
        return integer_value
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    user_input = input("Enter an integer: ")

    try:
        result = convert_to_integer(user_input)
        print(f"Integer value: {result}")
    except ValueError as e:
        print(e)
