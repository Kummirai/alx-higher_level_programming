#!/bin/bash
# Script that sends a GET request to passed URL and displays body of response
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id:98"
