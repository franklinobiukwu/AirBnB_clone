#!/usr/bin/python3
"""
Defines Test Class for BaseModel Class
"""
from models.base_model import BaseModel
import uuid
from datetime import datetime
from unittest import TestCase


class TestBaseModel(TestCase):
    """
    Test Class for BaseModel class
    """

    def test_to_dict(self):
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)
