#!/usr/bin/python3
"""Define rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Args:
        width: width of the rectangle
        height: height of rectangle

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Return the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raise:
        TypeError: if is not an integer
        ValueError: if is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Return the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raise:
        TypeError: if is not an integer
        ValueError: if is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
