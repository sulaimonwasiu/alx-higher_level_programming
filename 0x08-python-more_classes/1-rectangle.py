#!/usr/bin/python3
"""
And empty Module
"""


class Rectangle:
    """
    An empty rectangle class
    """
    def __init__(self, width=0,height=0):
        self.__width = self.validator(width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        value = cls.validator(value)
        self.__width = value

    def __str__(self):
        return f"This is a rectangle width a width of {self.width} cm."

    @staticmethod
    def validator(prop):
        if not isinstance(prop, int):
            raise TypeError("width must be an integer")
        if prop < 0:
            raise ValueError("width must be >= 0")
        return prop

