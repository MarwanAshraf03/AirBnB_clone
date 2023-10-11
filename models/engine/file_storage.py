#!/usr/bin/python3
import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Loads instances from json file"""
        if not path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            string = f.read()
            if not string:
                return
            fdict = json.loads(string)
        for key, value in fdict.items():
            self.__objects[key] = value
