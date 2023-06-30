#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id header.
Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
