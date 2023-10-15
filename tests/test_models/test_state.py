#!/usr/bin/python3
''' '''

import os
import unittest
from models.base_model import BaseModel
from models.state import State

class test_state(unittest.TestCase):
    '''
    
    '''

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)
        self.name = 'State'
        self.cls = State

    def test_instance_inheritance(self):
        ''' '''
        my_state = State()
        self.assertIsInstance(my_state, BaseModel)

    def test_instance_type(self):
        ''' '''
        my_state = State()
        self.assertIsInstance(my_state, self.cls)

    def test_name(self):
        ''' '''
        my_state = State()
        self.assertIsInstance(my_state.name, str)

if __name__ == "__main__":
    unittest.main()

