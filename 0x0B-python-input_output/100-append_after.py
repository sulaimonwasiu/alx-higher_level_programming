#!/usr/bin/python3
"""Append a new line of text to a file"""""


def append_after(filename="", search_string="", new_string=""):
    """Append a new line of text to a file"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
