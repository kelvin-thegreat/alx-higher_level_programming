#!/usr/bin/python3
"""Module for JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates an object from a given JSON file"""
    with open(filename) as filee:
        return json.load(filee)
