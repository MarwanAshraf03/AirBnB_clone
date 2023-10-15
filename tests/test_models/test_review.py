#!/usr/bin/python3
''' Review Module '''

import os
import unittest
from models.base_model import BaseModel
from models.review import Review


class test_Review(unittest.TestCase):
    ''' Review Class '''


    def __init__(self, *args, **kwargs):
        ''' initialization '''
        super().__init__(*args, **kwargs)
        self.name = 'Review'
        self.cls = Review

    def test_instance_type(self):
        ''' test that review is subclass of BaseModel'''
        my_review = Review()
        self.assertIsInstance(my_review, BaseModel)

    def test_text(self):
        ''' test that text attribute is in Review class '''
        my_review = Review()
        self.assertIsInstance(my_review.text, str)

    def test_place_id(self):
        ''' test that place_id attribute is in Review class '''
        my_review = Review()
        self.assertIsInstance(my_review.place_id, str)

    def test_user_id(self):
        ''' test that user_id attribute is in Review class '''
        my_review = Review()
        self.assertIsInstance(my_review.user_id, str)


if __name__ == "__main__":
    ''' '''
    unittest.main()
