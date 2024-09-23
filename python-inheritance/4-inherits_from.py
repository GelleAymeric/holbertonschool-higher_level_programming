#!/usr/bin/python3
"""Define is a subclass"""


def inherits_from(obj, a_class):
    """
        Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
