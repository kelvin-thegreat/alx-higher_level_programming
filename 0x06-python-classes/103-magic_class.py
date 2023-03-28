#!/usr/bin/python3
"""importing module"""
import math

class MagicClass:
    """defining a magicclass"""


    def __init__(self, radius=0):
        """writing"""
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) not in [int, float]:
            raise TypeError('radius must be a number')
        if value < 0:
            raise ValueError('radius must be >= 0')
        self.__radius = value

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return (2 * math.pi * self.__radius)
