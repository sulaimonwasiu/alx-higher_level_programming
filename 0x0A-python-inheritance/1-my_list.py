#!/usr/bin/python3
"""
Return list object in a sorted order
"""


class MyList(list):
    """
    Class inheriting the list class
    """
    def print_sorted(self):
        print(sorted(self))
