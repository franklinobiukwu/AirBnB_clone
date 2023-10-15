#!/usr/bin/python3
"""
Unit tests for User Class
"""
from unittest import TestCase
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(TestCase):
    """
    Test class to test User class
    """

    def test_new_instance(self):
        """
        Test for new instance
        """
        usr_obj = User()
        self.assertEqual(usr_obj.email, "")
        self.assertEqual(usr_obj.password, "")
        self.assertEqual(usr_obj.first_name, "")
        self.assertEqual(usr_obj.last_name, "")
