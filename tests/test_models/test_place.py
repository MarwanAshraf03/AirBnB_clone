#!/usr/bin/python3
''' '''

import os
import unittest
from models.base_model import BaseModel
from models.place import Place

class test_place(unittest.TestCase):
    '''
    
    '''

    def __init__(self, *args, **kwargs):
        ''' '''
        super().__init__(*args, **kwargs)
        self.name = 'Place'
        self.cls = Place

    def test_instance_type(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place, BaseModel)

    def test_city_id(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.city_id, str)

    def test_user_id(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.user_id, str)

    def test_name(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.name, str)

    def test_description(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.description, str)

    def test_number_rooms(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.number_rooms, int)
        self.assertGreaterEqual(my_place.number_rooms, 0)

    def test_number_bathrooms(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.number_bathrooms, int)
        self.assertGreaterEqual(my_place.number_bathrooms, 0)

    def test_max_guest(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.max_guest, int)
        self.assertGreaterEqual(my_place.max_guest, 0)

    def test_price_by_night(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.price_by_night, int)
        self.assertGreaterEqual(my_place.price_by_night, 0)

    def test_latitude(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.latitude, float)
        self.assertGreaterEqual(my_place.latitude, 0.0)

    def test_longitude(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.longitude, float)
        self.assertGreaterEqual(my_place.longitude, 0.0)

    def test_amenity_ids(self):
        ''' '''
        my_place = Place()
        self.assertIsInstance(my_place.amenity_ids, list)

if __name__ == "__main__":
    unittest.main()

