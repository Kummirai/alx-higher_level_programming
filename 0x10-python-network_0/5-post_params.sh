#!/bin/bash
# Script that sends a POST request to the URL passed and displays body of response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
