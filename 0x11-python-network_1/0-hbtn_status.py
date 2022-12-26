#!/usr/bin/python3
from urllib import request
""" Script that reads from a URL """


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as resp:
        data = resp.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode("utf-8")))
