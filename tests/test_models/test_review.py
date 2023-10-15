#!/usr/bin/python3
''' '''

import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    ''' '''

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)
        self.name = 'Review'
        self.cls = Review

    def test_instance_type(self):
        ''' '''
        my_review = Review()
        self.assertIsInstance(my_review, BaseModel)

    def test_text(self):
        ''' '''
        my_review = Review()
        self.assertIsInstance(my_review.text, str)

    def test_place_id(self):
        ''' '''
        my_review = Review()
        self.assertIsInstance(my_review.place_id, str)

    def test_user_id(self):
        ''' '''
        my_review = Review()
        self.assertIsInstance(my_review.user_id, str)


if __name__ == "__main__":
    ''' '''
    unittest.main()
