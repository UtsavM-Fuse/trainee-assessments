"""
Module: unique_characters_in_words

This module provides a function to create a set containing all unique 
characters present in a list of words.
"""


def unique_characters_in_words(words: list[str]) -> set[str]:
    """
    Create a set containing all unique characters present in the words.

    Args:
        words (list[str]): The list of words.

    Returns:
        set[str]: A set containing all unique characters.

    Examples:
        >>> words1 = ['hello', 'world', 'python']
        >>> unique_characters_in_words(words1)
        {'d', 'h', 'e', 'n', 'l', 'o', 'p', 'r', 't', 'w', 'y'}

        >>> words2 = ['apple', 'banana', 'orange']
        >>> unique_characters_in_words(words2)
        {'a', 'b', 'n', 'e', 'l', 'p', 'r', 'g', 'o'}
    """
    return {char for word in words for char in word}


def test_unique_characters_in_words():
    """
    This function is a test suite for the `unique_characters_in_words` function
    """
    # Test case 1: Normal case with mixed words
    words1 = ["hello", "world", "python"]
    assert unique_characters_in_words(words1) == {
        "d",
        "h",
        "e",
        "n",
        "l",
        "o",
        "p",
        "r",
        "t",
        "w",
        "y",
    }

    # Test case 2: Normal case with words of different lengths
    words2 = ["apple", "banana", "orange"]
    assert unique_characters_in_words(words2) == {
        "a",
        "b",
        "n",
        "e",
        "l",
        "p",
        "r",
        "g",
        "o",
    }

    # Test case 3: Empty list (should return an empty set)
    words3 = []
    assert unique_characters_in_words(words3) == set()

    # Test case 4: List with duplicate characters
    words4 = ["programming", "language", "python", "java"]
    assert unique_characters_in_words(words4) == {
        "p",
        "r",
        "o",
        "g",
        "a",
        "m",
        "i",
        "n",
        "l",
        "u",
        "e",
        "h",
        "t",
        "y",
        "j",
        "v",
    }

    # Test case 5: List with one word (should return unique characters of that word)
    words5 = ["hello"]
    assert unique_characters_in_words(words5) == {"h", "e", "l", "o"}

    # Test case 6: List with special characters
    words6 = ["@python", "javascript", "$python"]
    assert unique_characters_in_words(words6) == {
        "@",
        "p",
        "y",
        "t",
        "h",
        "o",
        "n",
        "j",
        "a",
        "v",
        "s",
        "c",
        "r",
        "i",
        "p",
        "$",
    }


if __name__ == "__main__":
    test_unique_characters_in_words()
    print("All test cases passed!")
