#!/usr/bin/python3
"""Base Module"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """BaseModel class"""

    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self, *args, **kwargs):
        """initializes Base class with id, time of creation, updating time"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                self.__setattr__(key, value)
                if key == "created_at" or key == "updated_at":
                    self.__setattr__(
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns string representation of class"""
        for key in self.__dict__:
            if type(self.__dict__[key]) is str:
                self.__dict__[key] = self.__dict__[key].replace('"', '')
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """sets the updating time to now"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns the dictionary representation of class"""
        ret = self.__dict__.copy()
        ret['__class__'] = __class__.__name__
        ret['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        ret['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return ret

    def update(self, name, value):
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
        self.__setattr__(name, value)
        storage.update(f'BaseModel.{self.id}', self.to_dict())
