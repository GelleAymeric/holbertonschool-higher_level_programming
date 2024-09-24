#!/usr/bin/env python3


class SwimMixin:
    """Mixin class to provide swimming ability to creatures."""

    def swim(self):
        """Indicates that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to provide flying ability to creatures."""

    def fly(self):
        """Indicates that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class, capable of swimming, flying, and roaring."""

    def swim(self):
        """method to indicate dragon swimming behavior."""
        print("The dragon swims!")

    def fly(self):
        """method to indicate dragon flying behavior."""
        print("The dragon flies!")

    def roar(self):
        """Indicates that the dragon roars."""
        print("The dragon roars!")
