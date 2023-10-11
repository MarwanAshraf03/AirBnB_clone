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
                setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    setattr(
                        self,
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
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """sets the updating time to now"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary representation of class"""
        ret = self.__dict__
        ret['__class__'] = __class__.__name__
        ret['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        ret['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return ret
