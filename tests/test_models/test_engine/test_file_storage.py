#!/usr/bin/python3
''' File Storage Module '''
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from os import path
from os import remove


class test_file_storage(unittest.TestCase):
    ''' file storage test '''
    def test_type(self):
        self.assertIsInstance(storage, FileStorage)

    def test_init(self):
        temp = FileStorage()
        self.assertEqual(type(temp).__name__, "FileStorage")

    def test_file_path(self):
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_save_base_model(self):
        b = BaseModel()
        self.assertEqual(storage.all()[f"BaseModel.{b.id}"].id, b.id)

    def test_save_base_model(self):
        u = User()
        self.assertEqual(storage.all()[f"User.{u.id}"].id, u.id)

    def test_save_base_model(self):
        p = Place()
        self.assertEqual(storage.all()[f"Place.{p.id}"].id, p.id)

    def test_save_base_model(self):
        a = Amenity()
        self.assertEqual(storage.all()[f"Amenity.{a.id}"].id, a.id)

    def test_save_base_model(self):
        s = State()
        self.assertEqual(storage.all()[f"State.{s.id}"].id, s.id)

    def test_save_base_model(self):
        c = City()
        self.assertEqual(storage.all()[f"City.{c.id}"].id, c.id)

    def test_save_base_model(self):
        r = Review()
        self.assertEqual(storage.all()[f"Review.{r.id}"].id, r.id)

    def storage_reset(self):
        if path.isfile("file.json"):
            remove("file.json")

    def test_save(self):
        b = BaseModel()
        dictionary = b.to_dict()
        b1 = BaseModel(**dictionary)
        b1.save()
        self.assertNotEqual(str(storage.all()[f"BaseModel.{b1.id}"]), str(b1))
        self.storage_reset()



if __name__ == "__main__":
    unittest.main()
