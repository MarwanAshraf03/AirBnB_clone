#!/usr/bin/python3
''' state module '''

import os
import unittest
from models.base_model import BaseModel
from models.state import State


class test_state(unittest.TestCase):
    ''' state module '''
    def __init__(self, *args, **kwargs):
        ''' initialization '''
        super().__init__(*args, **kwargs)
        self.name = 'State'
        self.cls = State

    def test_instance_inheritance(self):
        ''' test that state is subclass of BaseModel'''
        my_state = State()
        self.assertIsInstance(my_state, BaseModel)

    def test_instance_type(self):
        ''' test that instance of state is of the desired type '''
        my_state = State()
        self.assertIsInstance(my_state, self.cls)

    def test_name(self):
        ''' test that name attribute is in state class '''
        my_state = State()
        self.assertIsInstance(my_state.name, str)


if __name__ == "__main__":
    unittest.main()
