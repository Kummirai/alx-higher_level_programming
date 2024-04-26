#!/usr/bin/python3
"""
A script that fetches ALX Intranet status using requests package
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    print('Body response:')
    print('\t- type:', type(content))
    print('\t- content:', content)
