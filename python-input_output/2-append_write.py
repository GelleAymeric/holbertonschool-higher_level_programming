#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF8).

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The string to append to the file. Defaults to "".

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
