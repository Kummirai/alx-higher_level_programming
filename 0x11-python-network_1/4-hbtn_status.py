#!/usr/bin/python3
from requests import get
""" Script that fetches a URL """


if __name__ == "__main__":
    resp = get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
