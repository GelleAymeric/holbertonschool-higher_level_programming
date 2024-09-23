#!/usr/bin/python3
"""Define if the object is exactly an instance or not"""

def is_same_class(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: the class to compare
    
    Return:
        True if is an instance , otherwise false
    """
    if not isinstance(obj, a_class):
        return True
    else:
        return False
