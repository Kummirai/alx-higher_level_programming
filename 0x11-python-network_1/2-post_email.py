#!/usr/bin/python3
"""
A script that sends a POST request to a given URL with an email parameter and displays the response body.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line arguments
    email = sys.argv[2]  # Get the email from command line arguments

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create the request
    req = urllib.request.Request(url, data=data, method='POST')

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
