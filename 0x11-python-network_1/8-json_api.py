#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as
a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}  # Set q to empty string if no argument provided
    response = requests.post(url, data)

    res_type = response.headers['content-type']

    if type_res == 'application/json':
        result = response.json()
        _id = result.get('id')
        name = result.get('name')
        if (result != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
