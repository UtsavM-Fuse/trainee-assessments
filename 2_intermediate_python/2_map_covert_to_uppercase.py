"""
Uppercase Conversion Module

This module provides a function to convert all strings in a list to uppercase.
"""


def convert_to_uppercase(strings_list: list[str]) -> list[str]:
    """
        Convert all strings in the list to uppercase.

        Args:
            strings_list (list): A list of strings.

        Returns:
            list: A new list with all strings converted to uppercase.

    Examples:
            >>> input_list = ['hello', 'world', 'python']
            >>> convert_to_uppercase(input_list)
            ['HELLO', 'WORLD', 'PYTHON']

            >>> input_list = ['apple', 'banana', 'orange']
            >>> convert_to_uppercase(input_list)
            ['APPLE', 'BANANA', 'ORANGE']
    """
    return list(map(str.upper, strings_list))


def test_convert_to_uppercase():
    """
    This function is a test suite for the `convert_to_uppercase` function
    """
    # Test case 1: Basic conversion
    input_list1 = ["hello", "world", "python"]
    assert convert_to_uppercase(input_list1) == ["HELLO", "WORLD", "PYTHON"]

    # Test case 2: Conversion with different strings
    input_list2 = ["apple", "banana", "orange"]
    assert convert_to_uppercase(input_list2) == ["APPLE", "BANANA", "ORANGE"]

    # Test case 3: Conversion with empty strings
    input_list3 = ["hello", "", "world"]
    assert convert_to_uppercase(input_list3) == ["HELLO", "", "WORLD"]

    # Test case 4: Conversion with numbers (should raise AttributeError)
    try:
        input_list4 = ["hello", 123, "world"]
        convert_to_uppercase(input_list4)
    except (AttributeError, TypeError):
        assert True
    else:
        assert False, "Expected AttributeError but got no exception"


if __name__ == "__main__":
    test_convert_to_uppercase()
    print("All test cases passed!")
