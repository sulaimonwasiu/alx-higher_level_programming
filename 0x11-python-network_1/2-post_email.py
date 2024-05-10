#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    args = sys.argv
    url = args[1]
    email = args[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data, method='POST')

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
