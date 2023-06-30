#!/bin/bash
# Send the request using curl and capture the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
