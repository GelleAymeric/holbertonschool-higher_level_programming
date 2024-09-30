#!/usr/bin/python3
"""Module for reading and printing file contents."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
