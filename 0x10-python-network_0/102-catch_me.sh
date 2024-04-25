#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sLX PUT 0:5000/catch_me "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"
