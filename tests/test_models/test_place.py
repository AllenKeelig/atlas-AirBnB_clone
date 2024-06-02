#!/usr/bin/python3
'''
Test suites for place.py
'''

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Tests for Place class
    """

    def test_name(self):
        """
        Tests for name inputs
        """
        place = Place()
        place.name = "Cozy Apartment"
        self.assertEqual(place.name, "Cozy Apartment")

    def test_city_id(self):
        """
        Tests for city_id inputs
        """
        place = Place()
        place.city_id = "12345"
        self.assertEqual(place.city_id, "12345")


if __name__ == '__main__':
    unittest.main()
