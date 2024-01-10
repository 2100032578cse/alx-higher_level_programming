#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to file:
"""


import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item():
    """Check if the file 'add_item.json' exists"""
    if path.exists('add_item.json'):
        my_list = load_from_json_file('add_item.json')
    else:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, 'add_item.json')

if __name__ == "__main__":
    add_item()

"""from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    argv.pop(0)
    items.extend(argv)
    save_to_json_file(items, 'add_item.json')"""
