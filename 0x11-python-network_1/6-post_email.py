#!/usr/bin/python3
from requests import post
from sys import argv
"""
Script that sends a POST request to the URL passed in, with email
as a parameter, and displays the response
"""


if __name__ == "__main__":
    resp = post(argv[1], data={'email': argv[2]})
    print(resp.text)
