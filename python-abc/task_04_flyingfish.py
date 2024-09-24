#!/usr/bin/python3

class Fish:
    @classmethod
    def swim(self):
        """Method to indicate fish swimming."""
        print("The fish is swimming")
    
    @property
    def habitat(self):
        """Returns the habitat of the fish."""
        return "The fish lives in water"
        
class Bird:
    @classmethod
    def fly(self):
        """Method to indicate bird flying."""
        print("The bird is flying")
    
    @property
    def habitat(self):
        """Returns the habitat of the bird."""
        return "The bird lives in the sky"
        
class FlyingFish(Fish, Bird):
    def swim(self):
        """Method to indicate flying fish swimming."""
        print("The flying fish is swimming")
    
    def fly(self):
        """Method to indicate flying fish flying."""
        print("The flying fish is flying")

    @property
    def habitat(self):
        """Returns the habitat of the flying fish."""
        return "The flying fish lives both in water and the sky!"
