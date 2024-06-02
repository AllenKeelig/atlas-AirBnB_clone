import unittest
from state import BaseModel, State


class TestBaseModel(unittest.TestCase):

    def test_base_model_init(self):
        '''Test initialization of BaseModel.'''
        base_model = BaseModel(1)
        self.assertEqual(base_model.id, 1)

    def test_base_model_repr(self):
        '''Test __repr__ method of BaseModel.'''
        base_model = BaseModel(1)
        self.assertEqual(repr(base_model), "<BaseModel 1>")

class TestState(unittest.TestCase):

    def test_state_init(self):
        '''Test initialization of State.'''
        state = State(1, "California")
        self.assertEqual(state.id, 1)
        self.assertEqual(state.name, "California")

    def test_state_repr(self):
        '''Test __repr__ method of State.'''
        state = State(1, "California")
        self.assertEqual(repr(state), "<State 1: California>")


if __name__ == '__main__':
    unittest.main()
