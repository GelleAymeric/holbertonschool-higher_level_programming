#!/usr/bin/env python3

class CountedIterator:
    """An iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the count of items iterated over."""
        return self.count
