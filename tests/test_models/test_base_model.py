#!/usr/bin/pyton3
"""Unittest BaseModel class"""
import unittest
import os
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_atritt(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_to_dict(self):
        base = BaseModel()
        base.name = "Holberton"
        base.age = 89
        convert = base.to_dict()
        self.assertEqual(convert["id"], base.id)
        self.assertEqual(convert["name"], base.name)
        self.assertEqual(convert["age"], base.age)
        self.assertEqual(convert["updated_at"], base.updated_at.isoformat())
        self.assertEqual(convert["created_at"], base.created_at.isoformat())
        self.assertEqual(convert["__class__"], type(base).__name__)

    def tets_save(self):
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

if __name__ == "__main__":
    unittest.main()
