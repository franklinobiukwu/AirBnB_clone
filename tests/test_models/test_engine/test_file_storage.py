#!/usr/bin/python3
"""
Define Test Class of FileStorage class
"""
from models.engine.file_storage import FileStorage
from json import dump, dumps, load, loads
import os
from unittest import TestCase
from models.base_model import BaseModel


class TestFileStorage(TestCase):
    """
    Test Class for the File Storage class
    """

    def test_all(self):
        """Test if the all function returns an object"""
        store = FileStorage()
        result = store.all()
        self.assertIsInstance(result, dict)

    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    def test_new(self):
        """Test if new function adds an object to __objects"""
        new_model = BaseModel()
        self.storage.new(new_model)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Test if save and reload functions work"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()

    def test_get_file_path(self):
        """Test if get_file_path returns the correct file path"""
        self.assertEqual(self.storage.get_file_path(), "file.json")
