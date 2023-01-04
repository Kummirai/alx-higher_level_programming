#!/usr/bin/python3
from urllib.parse import urlencode
from urllib.request import urlopen
from sys import argv
"""
Script that sends a POST request to the URL passed in, with the email
as a paramater, and displays response
"""


if __name__ == "__main__":
    info = {'email': argv[2]}
    data = urlencode(info).encode("utf-8")
    with urlopen(argv[1], data) as resp:
        print(resp.read().decode("utf-8"))
