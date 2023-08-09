"""
Module: read_file_contents

This module provides a function to read and display the contents of a given file.
"""


def read_file_contents(filename: str) -> None:
    """
    Read and display the contents of the given file.

    Args:
        filename (str): The name of the file to be read.

    Raises:
        FileNotFoundError: If the specified file is not found.

    Examples:
        >>> read_file_contents("example.txt")
        File 'example.txt' contents:
        Line 1: This is line 1
        Line 2: This is line 2
        Line 3: This is line 3

        >>> read_file_contents("nonexistent_file.txt")
        File 'nonexistent_file.txt' not found. Please check the file name and try again.
    """
    try:
        with open(filename, "r") as file:
            print(f"File '{filename}' contents:")
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please check the file name and try again.")


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    read_file_contents(filename)
