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
