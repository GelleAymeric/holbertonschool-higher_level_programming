#!/usr/bin/python3

class Fish:

    def swim(self):
        """Method to indicate fish swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Returns the habitat of the fish."""
        print("The fish lives in water")
        
class Bird:

    def fly(self):
        """Method to indicate bird flying."""
        print("The bird is flying")

    def habitat(self):
        """Returns the habitat of the bird."""
        print("The bird lives in the sky")
        
class FlyingFish(Fish, Bird):
    def swim(self):
        """Method to indicate flying fish swimming."""
        print("The flying fish is swimming")
    
    def fly(self):
        """Method to indicate flying fish flying."""
        print("The flying fish is flying")

    def habitat(self):
        """Returns the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
