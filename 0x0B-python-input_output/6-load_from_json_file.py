#!/usr/bin/python3
"""Load from JSON file"""
import json


def load_from_json_file(filename):
    """Load from JSON file"""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
