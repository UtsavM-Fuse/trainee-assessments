"""
Module: json_operations

This module provides functions to create and manipulate JSON files.
"""

import json


def create_initial_json(filename: str, data: list[dict]) -> None:
    """
    Create an initial JSON file with the provided data.

    Args:
        filename (str): The name of the JSON file to be created.
        data (list[dict]): The list of dictionaries to be written as JSON data.

    Returns:
        None

    Examples:
        >>> data = [
        ...     {"name": "Ram", "age": 30},
        ...     {"name": "Sita", "age": 25}
        ... ]
        >>> create_initial_json("data.json", data)
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def add_to_json(filename: str, new_data: dict) -> None:
    """
    Read JSON data from a file, add the new dictionary to it, and write the updated data back to the same file.

    Args:
        filename (str): The name of the JSON file.
        new_data (dict): The dictionary to be added to the JSON data.

    Returns:
        None

    Examples:
        >>> data = [
        ...     {"name": "Ram", "age": 30},
        ...     {"name": "Sita", "age": 25}
        ... ]
        >>> new_data = {"name": "Lakshman", "age": 28}
        >>> add_to_json("data.json", new_data)
    """
    # Read JSON data from the file
    with open(filename, "r") as json_file:
        data = json.load(json_file)

    # Add the new dictionary to the JSON data
    data.append(new_data)

    # Write the updated data back to the same file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    initial_data = [{"name": "Ram", "age": 30}, {"name": "Sita", "age": 25}]
    create_initial_json("./data/data.json", initial_data)

    new_data = {"name": "Lakshman", "age": 28}
    add_to_json("./data/data.json", new_data)
