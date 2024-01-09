#!/usr/bin/python3
"""Defining Student class"""


class Student:
    """
        this is for student class body.
        it goes here
    """

    def __init__(self, first_name, last_name, age):
        """ student instance initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance
        """
         if attrs is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student Instance.
            Args:
                json (dictionary): reload data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
