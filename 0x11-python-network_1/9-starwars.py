#!/usr/bin/python3
'''
Script that takes in a string and sends a search request to the
Star Wars API
'''
import requests
from sys import argv

if __name__ == "__main__":
    values = {'search': argv[1]}
    resp = requests.get("https://swapi.co/api/people/", params=values)
    try:
        json = resp.json()
    except:
        print("Not a valid JSON")
    else:
        count = json["count"]
        print("Number of results: {}".format(count))
        for results in json["results"]:
                print(results["name"])
