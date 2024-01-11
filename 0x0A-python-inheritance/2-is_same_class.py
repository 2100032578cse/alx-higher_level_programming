#!/usr/bin/python3
""" defines obnj"""


def is_same_class(obj, a_class):
    """
    checks instance of a specified class

    Args:
    obj - object
    a_class - specified class

    Returns:
    True if object is exactly an instance of the specified class;
    otherwise False
    """
    return obj.__class__ is a_class
