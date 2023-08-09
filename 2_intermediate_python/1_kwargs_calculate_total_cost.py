"""
Total Cost Calculator Module

This module provides a function to calculate the total cost of items purchased from a store.
"""


def calculate_total_cost(**items) -> float:
    """
    Calculate the total cost of items purchased from a store.

    Args:
        **items: Keyword arguments representing item names as keys and item prices as values.

    Returns:
        float: The total cost of all items.

    Examples:
        >>> calculate_total_cost(apple=0.5, banana=0.3, orange=0.4)
        1.2
        >>> calculate_total_cost(laptop=1000, mouse=20, keyboard=50, monitor=200)
        1270.0
        >>> calculate_total_cost()
        0.0
    """
    total_cost = sum(items.values())
    return total_cost


def test_calculate_total_cost():
    """
    This function is a test suite for the `calculate_total_cost` function
    """
    # Test case 1: Calculate total cost for multiple items
    items1 = {"apple": 0.5, "banana": 0.3, "orange": 0.4}
    assert round(calculate_total_cost(**items1), 2) == 1.2

    # Test case 2: Calculate total cost for different items
    items2 = {"laptop": 1000, "mouse": 20, "keyboard": 50, "monitor": 200}
    assert calculate_total_cost(**items2) == 1270.0

    # Test case 3: Calculate total cost for no items
    items3 = {}
    assert calculate_total_cost(**items3) == 0.0

    # Test case 4: Calculate total cost for items with zero price
    items4 = {"pen": 0, "pencil": 0, "eraser": 0}
    assert calculate_total_cost(**items4) == 0.0

    # Test case 5: Calculate total cost for items with negative price
    items5 = {"shirt": -20, "shoes": -30, "hat": -10}
    assert calculate_total_cost(**items5) == -60.0

    print("All test cases passed!")


if __name__ == "__main__":
    test_calculate_total_cost()
