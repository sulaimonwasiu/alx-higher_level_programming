#!/usr/bin/python3
"""
This module provides a simple Locked class.
"""


class LockedClass:
    """A simple locked class"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            class_name = self.__class__.__name__
            msg = f"'{class_name}' object has no attribute '{name}'"
            raise AttributeError(msg)
        self.__dict__[name] = value
