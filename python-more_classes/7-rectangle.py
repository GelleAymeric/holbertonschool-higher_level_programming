#!/usr/bin/python3
"""Define rectangle"""


class Rectangle:
    """Represent a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
        width: width of the rectangle
        height: height of rectangle

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
    
    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)
    
    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calcultate and return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            print()
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns a string representation of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(
            str(self.print_symbol * self.__width) for _ in range(self.__height)
            )

    def __del__(self):
        """ Prints a message indicating that the rectangle is being deleted."""
        
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
