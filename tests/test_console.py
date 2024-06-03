#!/usr/bin/envpython3
"""
Unit tests for console using Mock module from python standard library
Checks console for capturing stdout into a StringIO object
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.cli = HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_quit(self):
        """Quit command"""
        self.assertTrue(self.cli.onecmd("quit"))

    def test_create_user(self):
        """Test creating a User instance"""
        self.mock_stdin.side_effect = iter(["User"])
        result = self.cli.onecmd("create User")
        self.assertIsNotNone(result)
        self.assertIsInstance(User.get(result), User)
        self.assertEqual(User.get(result).id, result)

    def test_show_user(self):
        """Test showing a User instance"""
        user_id = User().save().id
        self.mock_stdin.side_effect = iter(["User", user_id])
        result = self.cli.onecmd("show User {}".format(user_id))
        self.assertIn(str(User.get(user_id)), result)

    def test_destroy_user(self):
        """Test destroying a User instance"""
        user_id = User().save().id
        self.mock_stdin.side_effect = iter(["User", user_id])
        result = self.cli.onecmd("destroy User {}".format(user_id))
        self.assertFalse(User.get(user_id))

    def test_all_users(self):
        """Test listing all User instances"""
        users = [User(), User()]
        for user in users:
            user.save()
        self.mock_stdin.side_effect = iter(["User"])
        result = self.cli.onecmd("all User")
        for user in users:
            self.assertIn(str(user), result)

    def test_update_user(self):
        """Test updating a User instance"""
        user_id = User().save().id
        self.mock_stdin.side_effect = iter(["User", user_id, "new_name", "\"New Name\""])
        result = self.cli.onecmd("update User {} new_name \"New Name\"".format(user_id))
        self.assertEqual(User.get(user_id).new_name, "New Name")

if __name__ == '__main__':
    unittest.main()
