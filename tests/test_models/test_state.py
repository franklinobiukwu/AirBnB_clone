#!/usr/bin/python3
"""
Defines the test cases for State Class
"""
from models.state import State
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


class TestState(TestCase):
    """
    Test class for State Class
    """

    def test_new_instance(self):
        """
        Test case for new instance in State class
        """
        stat_obj = State()
        self.assertEqual(stat_obj.name, "")
