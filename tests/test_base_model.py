import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        '''Set up a new instance of BaseModel before each test.'''
        self.base_model = BaseModel()

    def test_id_is_unique(self):
        '''Test that id is unique for each instance.'''
        another_model = BaseModel()
        self.assertNotEqual(self.base_model.id, another_model.id)

    def test_created_at_initialization(self):
        '''Test that created_at is initialized correctly.'''
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_initialization(self):
        '''Test that updated_at is initialized correctly.'''
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        '''Test that save method updates the updated_at timestamp.'''
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)
        self.assertTrue(self.base_model.updated_at > old_updated_at)

    def test_delete_method(self):
        '''Test that delete method sets updated_at to None.'''
        self.base_model.delete()
        self.assertIsNone(self.base_model.updated_at)

    def test_str_method(self):
        '''Test that __str__ method returns the correct string representation.'''
        expected_str = "{}({}) - Created at: {}, Last updated at: {}".format(
            self.base_model.__class__.__name__, self.base_model.id, self.base_model.created_at, self.base_model.updated_at
        )
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
