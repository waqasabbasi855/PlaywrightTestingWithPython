import csv
import os
from typing import List, Dict


def append_dicts_to_csv(data: List[Dict], filename: str) -> None:
    """
    Appends a list of dictionaries to a CSV file.
    Creates the file with headers if it doesn't exist.

    :param data: List of dictionaries to write.
    :param filename: CSV file path.
    """
    if not data:
        print("No data to write.")
        return

    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

    print(f"Appended {len(data)} records to {filename}")
