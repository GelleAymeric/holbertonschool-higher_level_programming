#!/usr/bin/env python3

import math
"""import mathematical module"""
from abc import ABC, abstractmethod
"""import abstract"""


class Shape(ABC):
    """Create shape class"""
    @abstractmethod
    def area(self):
        """create abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """create abstract method perimeter"""
        pass


class Circle(Shape):
    """create class circle"""
    def __init__(self, radius):

        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(Shape):
    """"""
    print("Area : {}".format(Shape.area()))
    print("Perimeter : {}".format(Shape.perimeter()))
