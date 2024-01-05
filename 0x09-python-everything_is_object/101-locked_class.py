#!/usr/bin/python3
""" locked class task"""

class LockedClass:
    """ user will not be able to create anew class"""

    __slot__ = ["first_name"]
