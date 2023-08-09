"""
Module: csv_operations

This module provides functions to create and manipulate CSV files.
"""

import csv

data = [["John", "25"], ["Alice", "30"], ["Bob", "22"], ["Shyam", "12"]]
header = ["Name", "Age"]

# The filename for the new CSV file
filename = "./data/data.csv"

with open(filename, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Write the header to the CSV file
    writer.writerow(header)

    # Write the data to the CSV file
    writer.writerows(data)

print(f"New CSV file '{filename}' created and data written successfully.")


def filter_adults(input_file: str, output_file: str) -> None:
    """
    Read a CSV file, filter rows for individuals who are 18 years or older,
    and write the filtered rows to a new CSV file.

    Args:
        input_file (str): The name of the input CSV file.
        output_file (str): The name of the output CSV file for adults.

    Returns:
        None

    Examples:
        >>> filter_adults("data.csv", "adults.csv")
    """
    with open(input_file, mode="r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames

        # Filter rows for individuals who are 18 years or older
        filtered_rows = [row for row in reader if int(row["Age"]) >= 18]

    with open(output_file, mode="w", newline="") as csv_output:
        writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)


if __name__ == "__main__":
    input_file = "./data/data.csv"
    output_file = "./data/adults.csv"
    filter_adults(input_file, output_file)
