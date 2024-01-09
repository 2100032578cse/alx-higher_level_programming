#!/usr/bin/python3
""" for write file"""


def write_file(filename="", text=""):
    """ we use write and 'w' for writing """

    with open(filename, 'w', encoding = 'utf-8') as fl:
        return fl.write(text)
