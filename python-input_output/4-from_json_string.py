#!/usr/bin/python3
"""Module for JSON string parsing."""

import json


def from_json_string(my_str):
    """Parse a JSON string and return the corresponding Python object.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
