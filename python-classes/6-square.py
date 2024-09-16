#!/usr/bin/python3
"""Defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square

        Args:
            size (int): size of square
            position (tuple): position of the square

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0 or
            position contains negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Returns the size of the object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Raises:
            TypeError: If position is not a tuple of
            2 positive integers.
            ValueError: If position contains
            negative integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
