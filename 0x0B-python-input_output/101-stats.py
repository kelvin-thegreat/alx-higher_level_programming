#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

"""

def print_stats(size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

import sys

if __name__ == "__main__":
    count = 0
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()

            try:
                size = int(split_line[-1])
                total_size += size
            except ValueError:
                pass

            try:
                status_codes[split_line[-2]] += 1
            except (IndexError, KeyError):
                pass

            if count % 10 == 0:
                print("File size: {}".format(total_size))
                for k, v in sorted(status_codes.items()):
                    if v != 0:
                        print("{}: {}".format(k, v))

    except KeyboardInterrupt:
        pass

    finally:
        print("File size: {}".format(total_size))
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print("{}: {}".format(k, v))
