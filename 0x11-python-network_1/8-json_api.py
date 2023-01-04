#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    try:
        resp = post("http://0.0.0.0:5000/search_user", data={'q': q}).json()
    except:
        print("Not a valid JSON")
    else:
        if resp:
            print("[{}] {}".format(resp['id'], resp['name']))
        else:
            print("No result")
