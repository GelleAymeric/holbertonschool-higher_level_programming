#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """
        Initialize square

        Args:
            size (int): size of square

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Returns the size of the object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        Raise:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        The area is computed by multiplying the size of the square by itself.

        Returns:
        int: The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Print the square using the '#' character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
