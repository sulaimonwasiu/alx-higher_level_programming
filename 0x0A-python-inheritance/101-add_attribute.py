#!/usr/bin/python3
"""
Add and set attribute to an object
"""


def add_attribute(obj, a, v):
    """Add attribute to an object
    """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
