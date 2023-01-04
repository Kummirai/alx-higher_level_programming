#!/usr/bin/python3
"""
Sends a request to the URL passed in and displays the body
of the response
"""
from requests import get
from requests.exceptions import HTTPError
from sys import argv


if __name__ == "__main__":
    resp = get(argv[1])
    code = resp.status_code
    try:
        resp.raise_for_status()
        print(resp.text)
    except:
        print("Error code: {}".format(code))
