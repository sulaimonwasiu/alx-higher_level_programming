#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib.request as request
    import urllib.error as error

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
