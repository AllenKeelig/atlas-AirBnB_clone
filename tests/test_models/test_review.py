#!/usr/bin/python3
'''
Test suites for review.py
'''

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Tests for Review class
    """

    def test_text(self):
        """
        Tests for text inputs
        """
        review = Review()
        review.text = "Great experience, highly recommended!"
        self.assertEqual(review.text, "Great experience, highly recommended!")

    def test_rating(self):
        """
        Tests for rating inputs
        """
        review = Review()
        review.rating = 5
        self.assertEqual(review.rating, 5)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
