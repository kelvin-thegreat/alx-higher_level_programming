#!/usr/bin/python3
"""This idefines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student
        If attrs is a list of strings, represents only those attributes
        in the list
        """
        return self.__dict__
