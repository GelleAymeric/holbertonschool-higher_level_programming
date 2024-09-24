#!/usr/bin/env python3

from abc import ABC, abstractmethod
"""import abstract"""


class Animal(ABC):
    """create class animal"""
    @abstractmethod
    def sound(self):
        """create sound method"""
        pass


class Dog(Animal):
    """define class Dog"""
    def sound(self):
        """create sound of dog"""
        return "Bark"


class Cat(Animal):
    """define class cat"""
    def sound(self):
        """create sound of cat"""
        return "Meow"
