#!/usr/bin/python3
"""
file_storage Module
"""
import json
from os import path


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """init method doesn't do anything"""
        pass

    def all(self):
        """returns all the instances of the past"""
        return self.__objects.copy()

    def new(self, obj):
        """adds a new object to the __object dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """saves (serializes) __object dictionary to file.json"""
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Loads (deserializes) __object dictionary from file.json"""
        if not path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            string = f.read()
            if not string:
                return
            fdict = json.loads(string)
        for key, value in fdict.items():
            self.__objects[key] = value

    def remove(self, key):
        del self.__objects[key]

    def update(self, key, dictionary):
        self.__objects[key] = dictionary
