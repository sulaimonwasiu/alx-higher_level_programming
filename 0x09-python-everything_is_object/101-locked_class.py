#!/usr/bin/python3
"""
This module provides a simple Locked class.
"""


class LockedClass:
    """A simple Locked class"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            msg = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(msg)
        self.__dict__[name] = value
