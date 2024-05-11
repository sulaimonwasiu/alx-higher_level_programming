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

    if response.status_code == 200:
        try:
            data = response.json()
            if not data:
                print("No result")
            else:
                print(f"[{data['id']}] {data['name']}")
        except json.JSONDecodeError:
            print("Not a valid JSON")
    else:
        print(f"Error: Status code {response.status_code}")
