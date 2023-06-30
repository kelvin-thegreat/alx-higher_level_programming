#!/bin/bash
# send a POST request and display the body of the response using curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
