#!/usr/bin/python3
"""
Test suits for the base model
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def test_basic(self):
        """
        Tests basic inputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number], ["ALX", 89])

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))


if __name__ == '__main__':
    unittest.main()
