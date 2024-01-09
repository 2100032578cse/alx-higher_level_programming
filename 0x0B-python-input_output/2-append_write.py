#!/usr/bin/python3
""" for append file"""


def append_write(filename="", text=""):
    """ we use append and 'a' for writing """

    with open(filename, 'a', encoding='utf-8') as fl:
        return fl.write(text)
