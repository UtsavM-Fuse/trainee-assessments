"""
String Filtering Module

This module provides a function to filter strings with more than 5 characters from a given list.
"""


def filter_long_strings(strings_list: list[str]) -> list[str]:
    """
    Filter strings with more than 5 characters from the given list.

    Args:
        strings_list (list): A list of strings.

    Returns:
        list: A new list containing strings with more than 5 characters.

    Examples:
        >>> input_list = ['apple', 'banana', 'orange', 'grapes', 'kiwi', 'pear']
        >>> filter_long_strings(input_list)
        ['banana', 'orange', 'grapes']

        >>> input_list = ['python', 'java', 'c', 'c++', 'ruby']
        >>> filter_long_strings(input_list)
        ['python']
    """
    return list(filter(lambda x: len(x) > 5, strings_list))


def test_filter_long_strings():
    """
    This function is a test suite for the `filter_long_strings` function
    """
    # Test case 1: Filter long strings from the input list
    input_list1 = ["apple", "banana", "orange", "grapes", "kiwi", "pear"]
    assert filter_long_strings(input_list1) == ["banana", "orange", "grapes"]

    # Test case 2: Filter long strings with only one matching string
    input_list2 = ["python", "java", "c", "c++", "ruby"]
    assert filter_long_strings(input_list2) == ["python"]

    # Test case 3: No strings with more than 5 characters
    input_list3 = ["a", "b", "c", "d", "e"]
    assert not filter_long_strings(input_list3)

    # Test case 4: Empty input list
    input_list4 = []
    assert not filter_long_strings(input_list4)

    # Test case 5: All strings with more than 5 characters
    input_list5 = ["abcdef", "ghijklm", "nopqrst", "uvwxyz"]
    assert filter_long_strings(input_list5) == [
        "abcdef",
        "ghijklm",
        "nopqrst",
        "uvwxyz",
    ]


if __name__ == "__main__":
    test_filter_long_strings()
    print("All test cases passed!")
