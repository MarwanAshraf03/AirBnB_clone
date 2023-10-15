#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Define unittests for testing of BaseModel class"""

    def test_instantiation_with_None(self):
        """test instantiation with None"""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)

    def test_different_ids(self):
        """test comparison of two objects' ids"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_id_string(self):
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_id_string(self):
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_created_and_updated_at_datetime(self):
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime.datetime)
        self.assertIsInstance(b.updated_at, datetime.datetime)

    def test_str__(self):
        b = BaseModel()
        self.assertRegex(b.__str__(), "\[BaseModel\] \(.*\) \{.*\}")

    def test_save(self):
        b = BaseModel()
        before = b.updated_at
        b.save()
        after = b.updated_at
        self.assertNotEqual(before, after)













































































































if __name__ == '__main__':
    unittest.main()