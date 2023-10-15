#!/usr/bin/python3
"""
Defines the Test Class for Amenity Class
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from unittest import TestCase


class TestAmenity(TestCase):
    """
    Test Class for Amenity with Test cases
    """

    def test_new_instance(self):
        """
        Test case for new instance of Amenity
        """
        amenity_obj = Amenity()
        self.assertEqual(amenity_obj.name, "")
