#!/usr/bin/python3
""" This class will be the “base” of all other classes in this project"""

import json
import turtle
import tkinter as TK



class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """class Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            objs = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                objs = cls.from_json_string(file.read())
                return [cls.create(**obj) for obj in objs]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8") as file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    file.write("{},{},{},{},{}\n".format(obj.id, obj.width, obj.height, obj.x, obj.y))
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    file.write("{},{},{},{}\n".format(obj.id, obj.size, obj.x, obj.y))

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file to list of objects"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                objs = []
                for line in file:
                    fields = line.strip().split(",")
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(fields[0]), int(fields[1]), int(fields[2]), int(fields[3]), int(fields[4]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(fields[0]), int(fields[1]), int(fields[2]), int(fields[3]))
                    objs.append(obj)
                return objs
        except FileNotFoundError:
            return []
