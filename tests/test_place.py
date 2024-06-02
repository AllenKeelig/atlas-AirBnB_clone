import unittest
from place import BaseModel, Place


class TestBaseModel(unittest.TestCase):

    def test_base_model_init(self):
        '''Test initialization of BaseModel.'''
        base_model = BaseModel(1)
        self.assertEqual(base_model.id, 1)

    def test_base_model_repr(self):
        '''Test __repr__ method of BaseModel.'''
        base_model = BaseModel(1)
        self.assertEqual(repr(base_model), "<BaseModel 1>")


class TestPlace(unittest.TestCase):

    def test_place_init(self):
        '''Test initialization of Place.'''
        place = Place(1, "Beach House", "A nice beach house with a sea view", 3)
        self.assertEqual(place.id, 1)
        self.assertEqual(place.name, "Beach House")
        self.assertEqual(place.description, "A nice beach house with a sea view")
        self.assertEqual(place.num_rooms, 3)

    def test_place_repr(self):
        '''Test __repr__ method of Place.'''
        place = Place(1, "Beach House", "A nice beach house with a sea view", 3)
        self.assertEqual(repr(place), "<Place 1: Beach House, Rooms: 3>")


if __name__ == '__main__':
    unittest.main()
