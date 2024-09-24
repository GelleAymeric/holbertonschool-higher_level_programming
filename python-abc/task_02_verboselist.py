#!/usr/bin/python3


class VerboseList(list):
    """A list that prints messages on modifications."""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        number_item = len(item)
        super().extend(item)
        print("Extended the list with [{}] items.".format(number_item))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
            item = super().pop(index)
            print("Popped [{}] from the list".format(item))
            return item
