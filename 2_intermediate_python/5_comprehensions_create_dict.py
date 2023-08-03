def create_dictionary(keys_list: list[any], values_list: list[any]) -> dict[any, any]:
    """
    Create a dictionary using dictionary comprehension from two lists containing keys and values.

    Args:
        keys_list (list[any]): The list containing keys.
        values_list (list[any]): The list containing corresponding values.

    Returns:
        Dict[any, any]: A dictionary with keys and values from the two input lists.

    Examples:
        >>> keys_list = ['a', 'b', 'c']
        >>> values_list = [1, 2, 3]
        >>> create_dictionary(keys_list, values_list)
        {'a': 1, 'b': 2, 'c': 3}

        >>> keys_list = ['x', 'y', 'z']
        >>> values_list = [10, 20, 30]
        >>> create_dictionary(keys_list, values_list)
        {'x': 10, 'y': 20, 'z': 30}
    """
    return {key: value for key, value in zip(keys_list, values_list)}


def test_create_dictionary():
    # Test case 1: Normal case with strings and integers
    keys_list1 = ["a", "b", "c"]
    values_list1 = [1, 2, 3]
    assert create_dictionary(keys_list1, values_list1) == {"a": 1, "b": 2, "c": 3}

    # Test case 2: Normal case with strings and floats
    keys_list2 = ["x", "y", "z"]
    values_list2 = [10.0, 20.5, 30.75]
    assert create_dictionary(keys_list2, values_list2) == {
        "x": 10.0,
        "y": 20.5,
        "z": 30.75,
    }

    # Test case 3: Normal case with different data types
    keys_list3 = [1, "two", 3.14, True]
    values_list3 = [100, "hello", None, False]
    assert create_dictionary(keys_list3, values_list3) == {
        1: 100,
        "two": "hello",
        3.14: None,
        True: False,
    }

    # Test case 4: Empty lists (should return an empty dictionary)
    keys_list4 = []
    values_list4 = []
    assert create_dictionary(keys_list4, values_list4) == {}

    # Test case 5: Lists with different lengths (should truncate to the smaller length)
    keys_list5 = ["a", "b", "c"]
    values_list5 = [1, 2]
    assert create_dictionary(keys_list5, values_list5) == {"a": 1, "b": 2}

    # Test case 6: Lists with one element each
    keys_list6 = ["x"]
    values_list6 = [10]
    assert create_dictionary(keys_list6, values_list6) == {"x": 10}


if __name__ == "__main__":
    test_create_dictionary()
    print("All test cases passed!")
