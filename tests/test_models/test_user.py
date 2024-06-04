#!/usr/bin/python3
import os
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up test environment before each test.
        """
        self.storage = FileStorage()
        self.user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password123")

    def tearDown(self):
        """
        Clean up test environment after each test.
        """
        del self.user
        del self.storage

    def test_user_instance(self):
        """
        Test if User instance is created successfully.
        """
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.password, "password123")

    def test_user_greet(self):
        """
        Test the greet method of User class.
        """
        expected_greeting = "Hello, John Doe!"
        self.assertEqual(self.user.greet(), expected_greeting)
        custom_message = "Hi"
        expected_greeting = "Hi, John Doe"
        self.assertEqual(self.user.greet(custom_message), expected_greeting)

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
