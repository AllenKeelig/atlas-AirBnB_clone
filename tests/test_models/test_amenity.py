#!/usr/bin/python3
"""
Test suits for amenities
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Tests for amenities
    """

    def test_name(self):
        """
        Tests for name inputs
        """
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")


if __name__ == '__main__':
    unittest.main()
