#!/usr/bin/python3
'''test_user module'''

import os
import unittest
from models.base_model import BaseModel
from models.user import User


class test_user(unittest.TestCase):
    ''' test_user class '''

    def __init__(self, *args, **kwargs):
        ''' initialzation '''
        super().__init__(*args, **kwargs)
        self.name = 'User'
        self.cls = User

    def test_instance_type(self):
        ''' tests type of the instance '''
        my_user = User()
        self.assertIsInstance(my_user, BaseModel)

    def test_first_name(self):
        ''' tests that first_name attribute is in user class'''
        my_user = User()
        self.assertIsInstance(my_user.first_name, str)

    def test_last_name(self):
        ''' tests that last_name attribute is in user class'''
        my_user = User()
        self.assertIsInstance(my_user.last_name, str)

    def test_password(self):
        ''' tests that password attribute is in user class'''
        my_user = User()
        self.assertIsInstance(my_user.password, str)

    def test_email(self):
        ''' tests that email attribute is in user class'''
        my_user = User()
        self.assertIsInstance(my_user.email, str)


if __name__ == "__main__":
    unittest.main()
