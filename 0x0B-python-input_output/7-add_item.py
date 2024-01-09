#!/usr/bin/python3
"""Add item and save to JSON file"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    data = load_from_json_file("add_item.json")
    obj = data + sys.argv[1:]
    save_to_json_file(obj, "add_item.json")
else:
    if not os.path.exists("add_item.json"):
        save_to_json_file(sys.argv[1:], "add_item.json")
