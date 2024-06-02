#!/usr/bin/python3
'''
test for state.py
'''

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests for State class
    """

    def test_name(self):
        """
        Tests for name inputs
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main(
