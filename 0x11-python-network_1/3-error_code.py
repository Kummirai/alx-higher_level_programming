#!/usr/bin/python3
"""
A script that sends a request to a given URL and displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the HTTP status code.
"""
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line arguments
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
