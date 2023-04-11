#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a subclass of Rectangle"""

    def __init__(self, size):
        """Initializes a new Square instance with a given size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.integer_validator("size", value)
        self.__size = value
        self.width = value
        self.height = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
