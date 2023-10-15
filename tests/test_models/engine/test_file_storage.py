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
        storage = FileStorage()
        m1 = BaseModel()
        m2 = BaseModel()
        dic = {}
        dic[f"{type(m1).__name__}.{m1.id}"] = m1
        dic[f"{type(m2).__name__}.{m2.id}"] = m2
        self.assertEqual(dic, storage.all())

if __name__ == '__main__':
    unittest.main()
