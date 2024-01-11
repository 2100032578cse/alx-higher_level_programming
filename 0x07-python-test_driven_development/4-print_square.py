#!/usr/bin/python3
"""
This modeule is for printing square
on
"""


def print_square(size):
    """ this module print square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(size * ("#" * size + "\n"), end="")
