#!/usr/bin/python3
"""
A script that sends a POST request to a given URL with an email parameter and displays the response body.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line arguments
    email = sys.argv[2]  # Get the email from command line arguments

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Send the POST request
    response = requests.post(url, data=data)

    # Display the response body
    print(response.text)
