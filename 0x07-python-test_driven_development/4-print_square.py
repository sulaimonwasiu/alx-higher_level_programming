#!/usr/bin/python3
"""
Print Squares
"""


def print_square(size):
    """
    Print Square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif (type(size) is float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print()
