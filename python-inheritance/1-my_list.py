#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """
    method to print sorted list
    """
    
    def print_sorted(self):
        """
        print the list
        """
        print(sorted(self))
