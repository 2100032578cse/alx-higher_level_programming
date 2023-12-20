#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area with the position method """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes attribute size """
        self.size = size
        self.position = position

    def area(self):
        """func to claculate the area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """square related getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """the attribute size initialization """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """here is getter of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position attribute initialized"""
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print method reqired"""
        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(0, self.size):
                for e in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
