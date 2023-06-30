#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request to the passed URL
Usage: ./6-post_email.py <URL> <email>

"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)
    body = response.text

    print("Response Body:")
    print(body)

