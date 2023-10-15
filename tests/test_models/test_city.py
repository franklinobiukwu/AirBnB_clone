#!/usr/bin/python3
"""
Defines the Test Class for City Class
"""
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from unittest import TestCase


class TestCity(TestCase):
    """
    Test class for City Class
    """

    def test_new_instance(self):
        """
        Test Case for new instance in City Class
        """

        city_obj = City()
        self.assertEqual(city_obj.state_id, "")
        self.assertEqual(city_obj.name, "")
