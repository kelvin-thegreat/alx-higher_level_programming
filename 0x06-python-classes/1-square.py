#!/usr/bin/python3
class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Constructs a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
