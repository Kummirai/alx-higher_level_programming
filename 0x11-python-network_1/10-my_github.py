#!/usr/bin/python3
'''
Script that takes your Github credentials and uses the Github API
to display your id
'''
import requests
from sys import argv


if __name__ == "__main__":
    user_id = requests.get("https://api.github.com/user",
                           auth=(argv[1], argv[2]))
    try:
        resp = user_id.json()
    except:
        print("Not a valid JSON")
    else:
        print(resp.get('id'))
