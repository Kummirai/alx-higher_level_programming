#!/usr/bin/python3
"""
A script that sends an HTTP request to a given URL and displays the value of the X-Request-Id variable from the response header.
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line arguments
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print("X-Request-Id value:", x_request_id)
