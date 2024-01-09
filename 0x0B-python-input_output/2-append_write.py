#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    Write to a file
    Append: if file exists
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
