#!/usr/bin/python3
"""
Defines The Testcase for the Place Class
"""
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel
from unittest import TestCase


class TestPlace(TestCase):
    """
    Test Class for Place Class
    """

    def test_new_instance(self):
        """
        Test case for new instance for place
        """

        place_obj = Place()
        self.assertEqual(place_obj.city_id, "")
        self.assertEqual(place_obj.user_id, "")
        self.assertEqual(place_obj.name, "")
        self.assertEqual(place_obj.description, "")
        self.assertEqual(place_obj.number_rooms, 0)
        self.assertEqual(place_obj.number_bathrooms, 0)
        self.assertEqual(place_obj.max_guest, 0)
        self.assertEqual(place_obj.price_by_night, 0)
        self.assertEqual(place_obj.latitude, 0.0)
        self.assertEqual(place_obj.longitude, 0.0)
        self.assertEqual(place_obj.amenity_ids, [])
