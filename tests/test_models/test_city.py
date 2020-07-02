#!/usr/bin/python3
"""User tests"""


from models.city import City
from tests.test_models.test_base_model import TestBase
import os
import unittest


class TestCity (TestBase):
    """City tests"""

    def __init__(self, *args, **kwargs):
        """City tests"""

        super().__init__(*args, **kwargs)
        self._cls = City
        self._name = 'City'

    def test_permissions(self):
        """City tests"""
        is_read_true = os.access('models/city.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/city.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access('models/city.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_instance(self):
        """City tests"""
        my_city = City()
        self.assertIsInstance(my_city, City)
