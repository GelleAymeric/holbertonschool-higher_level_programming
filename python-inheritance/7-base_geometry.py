#!/usr/bin/python3
"""defines a base class for geometry-related classes."""


class BaseGeometry:
    """A base class for geometry operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an exception with the message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
