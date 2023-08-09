"""
String Concatenation Module

This module provides a function for concatenating any number of strings into a single string.
"""


def concat_strings(*args: str) -> str:
    """
    Concatenate any number of strings into a single string.

    Args:
        *args: Any number of strings.

    Returns:
        The concatenated string.

    Examples:
        >>> concat_strings("Hello", " ", "World")
        'Hello World'
        >>> concat_strings("Python", " ", "is", " ", "awesome!")
        'Python is awesome!'
        >>> concat_strings("I", " ", "love", " ", "Python", " ", "programming.")
        'I love Python programming.'
        >>> concat_strings()
        ''
    """
    return "".join(args)


def test_concat_strings():
    """
    This function is a test suite for the `concat_strings` function
    """
    # Test case 1: Basic concatenation
    result1 = concat_strings("Hello", " ", "World")
    assert result1 == "Hello World"

    # Test case 2: Concatenation with different strings
    result2 = concat_strings("Python", " ", "is", " ", "awesome!")
    assert result2 == "Python is awesome!"

    # Test case 3: Concatenation with a mix of words
    result3 = concat_strings("I", " ", "love", " ", "Python", " ", "programming.")
    assert result3 == "I love Python programming."

    # Test case 4: Concatenation with an empty string
    result4 = concat_strings("Hello", "", "World")
    assert result4 == "HelloWorld"

    # Test case 5: Concatenation with no arguments
    result5 = concat_strings()
    assert result5 == ""

    # Test case 6: Concatenation with numbers (should raise TypeError)
    try:
        concat_strings("Python", " ", 3.7)
    except TypeError:
        assert True
    else:
        assert False, "Expected TypeError but got no exception"


if __name__ == "__main__":
    test_concat_strings()
    print("All test cases passed!")
