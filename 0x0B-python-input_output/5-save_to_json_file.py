#!/usr/bin/python3
"""Save to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """Save to JSON file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
