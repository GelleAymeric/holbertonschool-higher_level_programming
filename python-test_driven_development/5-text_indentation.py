#!/usr/bin/python3
"""Module for text_indentation function"""


def text_indentation(text):
    """
    Add new line after special characters

    Args:
    text (str): is a text
    char: list of char

    Returns:
    print new line when function write special character

    Raises:
    TypeError: if is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".,?:":
            result += "\n\n"
    print(result)
