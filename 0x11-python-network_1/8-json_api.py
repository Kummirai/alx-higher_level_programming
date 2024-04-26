#!/usr/bin/python3
"""
A script that sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
Displays the id and name from the response if valid JSON and not empty.
"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create the data dictionary with the letter parameter
    data = {'q': letter}

    # Send the POST request
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            user_id = json_response.get('id')
            user_name = json_response.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
