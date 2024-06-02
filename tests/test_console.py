import unittest
from unittest.mock import patch
from io import StringIO
import sys
from my_console import MyConsole


class TestMyConsole(unittest.TestCase):
    
    def setUp(self):
        '''Set up a new instance of MyConsole before each test.'''
        self.console = MyConsole()

    @patch('sys.stdout', new_callable=StringIO)
    def test_greet_command(self, mock_stdout):
        '''Test the greet command.'''
        self.console.onecmd("greet TestUser")
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, TestUser")

    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_command(self, mock_stdout):
        '''Test the exit command.'''
        result = self.console.onecmd("exit")
        self.assertEqual(mock_stdout.getvalue().strip(), "Exiting...")
        self.assertTrue(result)

    def test_cmdloop(self):
        '''Test the command loop.'''
        with patch('builtins.input', side_effect=['exit']):
            with patch('sys.stdout', new_callable=StringIO):
                self.console.cmdloop()

if __name__ == '__main__':
    unittest.main()
