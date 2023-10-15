#!/usr/bin/python3
''' '''

import os
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    ''' '''

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)
        self.name = 'Amenity'
        self.cls = Amenity

    def test_instance_type(self):
        ''' '''
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, BaseModel)

    def test_name(self):
        ''' '''
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity.name, str)


if __name__ == "__main__":
    unittest.main()
