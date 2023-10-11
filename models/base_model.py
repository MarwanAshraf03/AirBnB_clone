#!/usr/bin/python3
"""Base Module"""
import json
from os import path
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class"""

    id = ""
    created_at = ""
    updated_at = ""

    def __init__(self):
        """
        initializes Base class with id, time of creation, updating time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        converts class to string
        """
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        sets the updating time to now
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns the dictionary representation of class
        """
        ret = self.__dict__
        ret['__class__'] = __class__.__name__
        ret['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        ret['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return ret
