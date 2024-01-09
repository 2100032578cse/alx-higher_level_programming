#!/usr/bin/python3
"""read from obj file"""

import json


def load_from_json_file(filename):
    """ load from json file"""
    with open(filename, "r") as fl:
        ans = json.loads(fl.read())
    return ans
