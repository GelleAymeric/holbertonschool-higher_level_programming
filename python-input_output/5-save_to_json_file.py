#!/usr/bin/python3
"""Module for saving Python objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file to save the object to.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
