#!/usr/bin/python3
from requests import get
from sys import argv
"""
Script sends a request to the URL passed in
and displays the X-Request-Id variable
"""


if __name__ == "__main__":
    resp = get(argv[1])
    print(resp.headers.get('X-Request-Id'))
