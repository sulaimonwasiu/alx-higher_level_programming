#!/usr/bin/python3
"""Write a Python script that fetches resources
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
    else:
        print(f"Error: Status code {response.status_code}")
