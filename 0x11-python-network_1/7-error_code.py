#!/usr/bin/python3
"""
A script that sends a request to a given URL and displays the body of the response.
Handles HTTP status codes greater than or equal to 400.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line arguments
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
