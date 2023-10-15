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
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        for i, j in self.__objects.items():
            self.__objects[i] = j.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(self.__objects, f)
        self.reload()

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        classes = {
            "BaseModel": BaseModel,
            "User": User
        }
        if not path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            dictionary = f.read()
        if not dictionary:
            return
        dictionary = json.loads(dictionary)
        for i, j in dictionary.items():
            self.__objects[i] = classes[j["__class__"]](**j)

    def remove(self, key):
        del self.__objects[key]
        self.save()
