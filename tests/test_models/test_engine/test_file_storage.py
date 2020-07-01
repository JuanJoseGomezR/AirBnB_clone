#!/usr/bin/python3
""" Unittest for file storage """
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Juan"
        cls.base.num = 18

    @classmethod
    def teardown(cls):
        """tear down"""
        del cls.base

    def tearDown(self):
        """ tear down test """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """ pep8 test """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_method_BaseModel(self):
        """ method test """
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """ init test """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaesModel(self):
        """ save test """
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

if __name__ == "__main__":
    unittest.main()
