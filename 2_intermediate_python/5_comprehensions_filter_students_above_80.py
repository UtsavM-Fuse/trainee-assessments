"""
Module: filter_students_above_80

This module provides a function to filter students who scored more than 80 from a dictionary.
"""


def filter_students_above_80(scores_dict: dict[str, int]) -> dict[str, int]:
    """
    Create a new dictionary containing only the students who scored more than 80.

    Args:
        scores_dict (dict[str, int]): A dictionary with students' names as keys and
        their respective scores as values.

    Returns:
        dict[str, int]: A new dictionary with students who scored more than 80.

    Examples:
        >>> scores = {'Alice': 85, 'Bob': 70, 'Charlie': 90, 'David': 75}
        >>> filter_students_above_80(scores)
        {'Alice': 85, 'Charlie': 90}
    """
    return {name: score for name, score in scores_dict.items() if score > 80}


def test_filter_students_above_80():
    """
    This function is a test suite for the `filter_students_above_80` function
    """
    # Test case 1: Normal case with students above and below 80
    scores1 = {"Alice": 85, "Bob": 70, "Charlie": 90, "David": 75}
    assert filter_students_above_80(scores1) == {"Alice": 85, "Charlie": 90}

    # Test case 2: Normal case with all students above 80
    scores2 = {"John": 95, "Emma": 100, "Michael": 88, "Sophia": 92}
    assert filter_students_above_80(scores2) == {
        "John": 95,
        "Emma": 100,
        "Michael": 88,
        "Sophia": 92,
    }

    # Test case 3: Normal case with all students below 80 (should return an empty dictionary)
    scores3 = {"Mary": 78, "William": 79, "Olivia": 76, "James": 77}
    assert filter_students_above_80(scores3) == {}

    # Test case 4: Empty dictionary (should return an empty dictionary)
    scores4 = {}
    assert filter_students_above_80(scores4) == {}

    # Test case 5: One student above 80
    scores5 = {"Ethan": 95}
    assert filter_students_above_80(scores5) == {"Ethan": 95}


if __name__ == "__main__":
    test_filter_students_above_80()
    print("All test cases passed!")
