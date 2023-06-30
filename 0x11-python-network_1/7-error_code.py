#!/usr/bin/python3
"""Script that Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handling HTTP erroris.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
