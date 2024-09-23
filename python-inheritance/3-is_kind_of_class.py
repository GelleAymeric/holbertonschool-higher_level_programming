#!/usr/bin/python3
"""function that returns if is an instance or not"""


def is_kind_of_class(obj, a_class):
    """
      Args:
        obj: object to check
        a_class: the class to compare

    Return:
         True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    if not isinstance(obj, a_class):
        return True
    else:
        return False
