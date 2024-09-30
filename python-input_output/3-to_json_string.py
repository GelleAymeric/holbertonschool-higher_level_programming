#!/usr/bin/python3
"""Module for JSON string conversion."""

import json


def to_json_string(my_obj):
    """Convert an object to its JSON string representation.

    Args:
        my_obj: The object to be converted to JSON string.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
