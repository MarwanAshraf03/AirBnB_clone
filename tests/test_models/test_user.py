#!/usr/bin/python3
''' '''

import os
import unittest
from models.base_model import BaseModel
from models.user import User


class test_user(unittest.TestCase):
    ''' '''

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)
        self.name = 'User'
        self.cls = User

    def test_instance_type(self):
        ''' '''
        my_user = User()
        self.assertIsInstance(my_user, BaseModel)

    def test_first_name(self):
        ''' '''
        my_user = User()
        self.assertIsInstance(my_user.first_name, str)

    def test_last_name(self):
        ''' '''
        my_user = User()
        self.assertIsInstance(my_user.last_name, str)

    def test_password(self):
        ''' '''
        my_user = User()
        self.assertIsInstance(my_user.password, str)

    def test_email(self):
        ''' '''
        my_user = User()
        self.assertIsInstance(my_user.email, str)


if __name__ == "__main__":
    unittest.main()
