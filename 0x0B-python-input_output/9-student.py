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

    def to_json(self):
        """ for dict representation"""
        return self.__dict__
