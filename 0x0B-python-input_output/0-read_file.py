#!/usr/bin/python3
"""func for reading a file"""


def read_file(filename=""):
    """ read file function is used"""

    with open(filename, 'r', encoding = 'utf-8') as fl:
        for a in fl:
            print(a, end="")
    fl.close()
