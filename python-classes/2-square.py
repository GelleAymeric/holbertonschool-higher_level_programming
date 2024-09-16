#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        initialise square

        Args:
        size (int): size of square

        Raise:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size