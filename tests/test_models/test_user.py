#!/usr/bin/python3
'''
test for user.py
'''

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests for User class
    """

    def test_email(self):
        """
        Tests for email inputs
        """
        user = User()
        user.email = "john.doe@example.com"
        self.assertEqual(user.email, "john.doe@example.com")

    def test_password(self):
        """
        Tests for password inputs
        """
        user = User()
        user.password = "securepassword123"
        self.assertEqual(user.password, "securepassword123")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
