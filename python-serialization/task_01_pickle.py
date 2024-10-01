#!/usr/bin/python3


"""
This module defines a CustomObject class
with serialization capabilities.
"""

import pickle


class CustomObject:
    """A class to represent a person with
    serialization capabilities."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The person's name.
            age (int): The person's age.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file
            to save the serialized object.

        Returns:
            bool or None: True if serialization
            is successful, None if an error occurs.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file.

        Args:
            filename (str): The name of the file
            to load the serialized object from.

        Returns:
            CustomObject or None: The deserialized object if successful,
            None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None


# Example usage (can be commented out or removed)
if __name__ == "__main__":
    # Create an instance of CustomObject
    person = CustomObject("John", 25, True)

    # Display the object's attributes
    print("Original object:")
    person.display()

    # Serialize the object to a file
    if person.serialize("person.pkl"):
        print("\nObject serialized successfully.")

    # Deserialize the object from the file
    loaded_person = CustomObject.deserialize("person.pkl")

    if loaded_person:
        print("\nDeserialized object:")
        loaded_person.display()

    # Test error handling with non-existent file
    non_existent = CustomObject.deserialize("non_existent.pkl")
    if non_existent is None:
        print("\nHandled non-existent file correctly.")
