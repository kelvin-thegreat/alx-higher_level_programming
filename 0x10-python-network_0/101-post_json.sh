#!/bin/bash
# Send the POST request with the JSON data in the request body using curl
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
