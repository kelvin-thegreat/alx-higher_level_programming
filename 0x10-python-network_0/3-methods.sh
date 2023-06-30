#!/bin/bash
# Script to display all HTTP methods that the server will accept via curl
curl -sI "$1" | cut -d " " -f 2- | grep "Allow"
