#!/usr/bin/python3
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv
"""
Script that sends a request to the URL passed in and displays
the response
"""


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as error:
            print("Error code: {}".format(error.code))
