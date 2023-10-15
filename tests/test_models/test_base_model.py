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
        """Test if instance method to_dict returns a dictionary"""

        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_inst_attr(self):
        """Test if instance has attributes"""

        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)

    def test_obj_id(self):
        """Test if ids of two objects are different"""

        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save(self):
        """Test case for save method"""
        obj = BaseModel()
        before_save = obj.updated_at
        obj.save()
        self.assertNotEqual(before_save, obj.updated_at)

    def test_create_instance_from_dict(self):
        """Test that creates an instance from dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)
