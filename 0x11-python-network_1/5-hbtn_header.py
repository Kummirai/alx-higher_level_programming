#!/usr/bin/python3
"""
A script that sends a request to a given URL and displays the value of the X-Request-Id variable from the response header.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line arguments
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
