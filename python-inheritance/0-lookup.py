#!/usr/bin/python3
""" returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    Args:
        obj: inspect object

    Return:
        list of attributes and methods of the object
    """
    return dir(obj)
