#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return characters written.

    Args:
        filename (str): The name of the file to write. Defaults to "".
        text (str): The string to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
