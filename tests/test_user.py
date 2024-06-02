import unittest
from unittest.mock import patch
from io import StringIO
from user import User


class TestUser(unittest.TestCase):

    def test_user_init(self):
        '''Test initialization of User.'''
        user = User("John", "Doe", "john.doe@example.com", "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.password, "password123")

    def test_greet_default(self):
        '''Test greet method without custom message.'''
        user = User("John", "Doe", "john.doe@example.com", "password123")
        self.assertEqual(user.greet(), "Hello, John Doe!")

    def test_greet_custom_message(self):
        '''Test greet method with custom message.'''
        user = User("John", "Doe", "john.doe@example.com", "password123")
        self.assertEqual(user.greet("Welcome"), "Welcome, John Doe")

    def test_create_user(self):
        '''Test create_user method.'''
        user = User.create_user("Jane", "Doe", "jane.doe@example.com", "password456")
        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "jane.doe@example.com")
        self.assertEqual(user.password, "password456")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_users(self, mock_stdout):
        '''Test display_users method.'''
        user1 = User("John", "Doe", "john.doe@example.com", "password123")
        user2 = User("Jane", "Doe", "jane.doe@example.com", "password456")
        User.display_users([user1, user2])
        expected_output = (
            "Name: John Doe\n"
            "Email: john.doe@example.com\n"
            "Hello, John Doe!\n"
            "Name: Jane Doe\n"
            "Email: jane.doe@example.com\n"
            "Hello, Jane Doe!\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
