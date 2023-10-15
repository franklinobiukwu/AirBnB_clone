#!/usr/bin/python3
"""
Defines Test Class for Review Class
"""
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from unittest import TestCase


class TestReview(TestCase):
    """
    Test Class for Review class
    """

    def test_new_instance(self):
        """
        Test method for a new instance
        """
        review_obj = Review()
        self.assertEqual(review_obj.place_id, "")
        self.assertEqual(review_obj.user_id, "")
        self.assertEqual(review_obj.text, "")
