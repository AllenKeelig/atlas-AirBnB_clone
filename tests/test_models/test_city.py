#!/usr/bin/python3
"""
Test suits for cities
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Tests for cities
    """

    def test_name(self):
        """
        Tests for name inputs
        """
        city = City()
        city.name = "New York"
        self.assertEqual(city.name, "New York")

    def test_state_id(self):
        """
        Tests for state_id inputs
        """
        city = City()
        city.state_id = "NY"
        self.assertEqual(city.state_id, "NY")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
