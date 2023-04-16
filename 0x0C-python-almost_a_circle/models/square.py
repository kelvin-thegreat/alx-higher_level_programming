#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape, which inherits from Rectangle.

    Attributes:
        size (int): The size of the square (same as width and height).
        x (int): The x-coordinate of the top-left corner.
        y (int): The y-coordinate of the top-left corner.
        id (int): The unique identifier of the instance.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initializes a new instance of the Square class.
        __str__(self): Returns the string representation of the Square instance.
        update(self, *args, **kwargs): Updates the attributes of the Square instance.
        to_dictionary(self): Returns the dictionary representation of the Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (same as width and height).
            x (int, optional): The x-coordinate of the top-left corner (default: 0).
            y (int, optional): The y-coordinate of the top-left corner (default: 0).
            id (int, optional): The unique identifier of the instance (default: None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute, which is the same as width and height.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute, which assigns the value to both width and height.

        Args:
            value (int): The new value of the size attribute.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    # Validation for width and height is inherited from Rectangle class
    # No need to override the validation methods

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: List of arguments to update the attributes (id, size, x, y).
            **kwargs: Dictionary of keyword arguments to update the attributes.

        Notes:
            * If args is not empty, it is used to update the attributes in the order (id, size, x, y).
            * If kwargs is not empty and args is empty, kwargs is used to update the attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

