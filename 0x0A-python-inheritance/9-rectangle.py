#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry"""


class BaseGeometry:
    """This class represents a base geometry"""

    def area(self):
        """Method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class represents a rectangle"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Computes the area of a Rectangle instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """Returns a string representation of a Rectangle instance"""
        return self.__str__()
