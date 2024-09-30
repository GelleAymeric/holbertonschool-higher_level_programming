#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): The attributes to represent.

        Returns:
            dict: The dictionary representation of the Student.
        """
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {
                k: getattr(self, k)
                for k in attrs
                if hasattr(self, k)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
