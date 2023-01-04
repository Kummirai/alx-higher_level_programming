#!/bin/bash
# Sends a request to the passed in URL and displays size of the body response
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
