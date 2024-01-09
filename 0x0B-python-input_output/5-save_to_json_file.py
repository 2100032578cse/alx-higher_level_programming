#!/usr/bin/python3
""" for saving to json file"""

import json


def save_to_json_file(my_obj, filename):
    """ for saving to a json file"""
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
