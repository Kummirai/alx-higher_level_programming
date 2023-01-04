#!/usr/bin/python3
from urllib import request
import sys
"""
Script that sends a request to the URL and displays the value
of the X-Request-Id variable
"""


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        print(resp.getheader('X-Request-Id'))
