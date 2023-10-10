#!/usr/bin/python3
"""Base Module"""
import json
from os import path


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes Base class with id

        Args:
        id: id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON encoding of list_dictionaries"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves list of objects to a file with name of: <Class Name>.json"""
        saved = []
        if list_objs:
            for i in list_objs:
                saved.append(i.to_dictionary())
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(saved))

    @staticmethod
    def from_json_string(json_string):
        """Decodes string from JSON notation to objects"""
        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates instance of any class that inherits Base class"""
        if cls.__name__ == "Rectangle":
            d = cls(1, 1)
        else:
            d = cls(1)
        d.update(**dictionary)
        return d

    @classmethod
    def load_from_file(cls):
        """Loads instances from json file"""
        fname = f"{cls.__name__}.json"
        ret = []
        if not path.isfile(fname):
            return ret
        with open(fname, "r", encoding="utf-8") as f:
            lst = cls.from_json_string(f.read())
        for i in lst:
            ret.append(cls.create(**i))
        return ret
