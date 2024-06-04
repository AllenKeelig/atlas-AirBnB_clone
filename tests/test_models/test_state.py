#!/usr/bin/python3
import os
import unittest
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime

class TestState(unittest.TestCase):
    def setUp(self):
        """
        Set up test environment before each test.
        """
        self.storage = FileStorage()
        self.state = State(name="California")

    def tearDown(self):
        """
        Clean up test environment after each test.
        """
        del self.state
        del self.storage

    def test_state_instance(self):
        """
        Test if State instance is created successfully.
        """
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertEqual(self.state.name, "California")

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
