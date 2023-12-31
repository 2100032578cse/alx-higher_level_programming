#!/usr/bin/python3

""" for class rectangle"""


class Rectangle:
    """ for methods"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """for area"""
        return self.width * self.height

    def perimeter(self):
        """for  perimeter of the rectangle."""

        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ for printing"""

        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """using eval"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ when rectangle is deleted"""

        print("Bye rectangle...")
