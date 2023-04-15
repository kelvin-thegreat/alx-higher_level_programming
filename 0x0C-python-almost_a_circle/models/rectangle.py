#!/usr/bin/python3
"""This module defines a class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""

        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance"""

        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the string representation of the Rectangle instance"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance"""

        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle instance"""

        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

