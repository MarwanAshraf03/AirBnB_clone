#!/usr/bin/python3
''' '''

import os
import unittest
from models.base_model import BaseModel
from models.city import City

class test_city(unittest.TestCase):
    '''
    
    '''

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)
        self.name = 'City'
        self.cls = City

    def test_instance_type(self):
        ''' '''
        my_city = City()
        self.assertIsInstance(my_city, BaseModel)

    def test_name(self):
        ''' '''
        my_city = City()
        self.assertIsInstance(my_city.name, str)

    def test_state_id(self):
        ''' '''
        my_city = City()
        self.assertIsInstance(my_city.state_id, str)

if __name__ == "__main__":
    unittest.main()

