#!/usr/bin/python3
"""Module to convert CSV files to JSON format"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it as 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:

        data = []

        with open(csv_filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                data.append(row)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
