def elementwise_product(list1: list[int], list2: list[int]) -> list[int]:
    """
    Create a new list containing the product of each element of the first list
    with the corresponding element in the second list.

    Args:
        list1 (list[int]): The first list of integers.
        list2 (list[int]): The second list of integers.

    Returns:
        list[int]: A new list containing the element-wise product.

    Examples:
        >>> list1 = [1, 2, 3, 4, 5]
        >>> list2 = [10, 20, 30, 40, 50]
        >>> elementwise_product(list1, list2)
        [10, 40, 90, 160, 250]

        >>> list1 = [2, 4, 6, 8]
        >>> list2 = [3, 3, 3, 3]
        >>> elementwise_product(list1, list2)
        [6, 12, 18, 24]
    """
    return [x * y for x, y in zip(list1, list2)]


def test_elementwise_product():
    # Test case 1: Normal case with positive integers
    assert elementwise_product([1, 2, 3], [10, 20, 30]) == [10, 40, 90]

    # Test case 2: Normal case with negative integers
    assert elementwise_product([-2, 4, -6], [3, -3, 3]) == [-6, -12, -18]

    # Test case 3: One empty list (should return an empty list)
    assert elementwise_product([1, 2, 3], []) == []

    # Test case 4: Lists with different lengths (should truncate to the smaller length)
    assert elementwise_product([1, 2, 3], [10, 20, 30, 40]) == [10, 40, 90]

    # Test case 5: Lists with one element each
    assert elementwise_product([5], [10]) == [50]

    # Test case 6: Lists with all elements as 0 (should return a list with 0s)
    assert elementwise_product([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

    # Test case 7: Lists with float numbers
    assert elementwise_product([1.5, 2.5, 3.5], [2, 3, 4]) == [3.0, 7.5, 14.0]

    # Test case 8: Lists with negative float numbers
    assert elementwise_product([-1.5, -2.5, -3.5], [-2, -3, -4]) == [3.0, 7.5, 14.0]

    # Test case 9: Lists with zero and positive numbers
    assert elementwise_product([0, 5, 0], [1, 0, 2]) == [0, 0, 0]

    # Test case 10: Lists with zero and negative numbers
    assert elementwise_product([0, -5, 0], [1, 0, -2]) == [0, 0, 0]


if __name__ == "__main__":
    test_elementwise_product()
    print("All test cases passed!")
