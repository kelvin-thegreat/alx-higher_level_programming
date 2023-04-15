#!/usr/bin/python3
"""Import the Base class from models.base module"""
from models.base import Base

"""Define a Rectangle class that inherits from the Base class"""
class Rectangle(Base):

    """Define the constructor that takes width, height, x, y, and id as arguments"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ # Call the constructor of the parent class (Base) with the id argument"""
        super().__init__(id)

        """Set the private instance attributes for width, height, x, and y"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """Define the getter and setter methods for the private width attribute"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private width attribute to the given value"""
        self.__width = value

    """Define the getter and setter methods for the private height attribute"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Set the private height attribute to the given value"""
        self.__height = value

    """Define the getter and setter methods for the private x attribute"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Set the private x attribute to the given value
        self.__x = value

    # Define the getter and setter methods for the private y attribute
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # Set the private y attribute to the given value
        self.__y = value


