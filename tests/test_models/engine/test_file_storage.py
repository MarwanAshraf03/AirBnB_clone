#!/usr/bin/python3
'''Unittests for file storage'''

import unittest
from models.base_model import BaseModel
from models import FileStorage
import json
import datetime


class TestFileStorage(unittest.TestCase):
    ''' '''

    def test_instance_type(self):
        ''' '''
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)        

    def test_all(self):
        ''' '''
        pass


if __name__ == '__main__':
    unittest.main()
