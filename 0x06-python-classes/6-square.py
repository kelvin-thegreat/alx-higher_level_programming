#!/usr/bin/python3
"""square module"""


class Square:
    """class used to represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance

        Args:
            size (int): size of the square
            position (tuple): position of the square

        Returns:
            None
        """

        self.size = size
        self.position = position

    def __str__(self):
        """Returns a string representation of the square"""

        res = ""
        if self.size == 0:
            return res

        for i in range(self.position[1]):
            res += "\n"

        for i in range(self.size):
            res += " " * self.position[0] + "#" * self.size + "\n"

        return res[:-1]

    @property
    def size(self):
        """Retrieves the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Computes the area of the square"""

        return self.size ** 2

    def my_print(self):
        """Prints the square using '#' character"""

        print(str(self))

