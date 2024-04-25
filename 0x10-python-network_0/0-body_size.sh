#!/bin/bash
# Sends a request to the passed in URL and displays size of the body response

URL=$1

IFS=$'\n' read -d "" body code  < <(curl -s -w "\n%{http_code}\n" "$URL")

echo "HTTP Code: $code"
echo "Response Body Size: ${#body} bytes"
