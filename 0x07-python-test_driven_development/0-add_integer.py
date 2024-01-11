#!/usr/bin/python3
"""
this is add_integer
modele
"""


def add_integer(a, b):
    """
    for adding two numbers
    """

    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("a must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a+b)
