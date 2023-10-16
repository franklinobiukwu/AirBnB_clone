#!/usr/bin/python3
"""
Define Test Class of FileStorage class
"""
from models.engine.file_storage import FileStorage
from json import dump, dumps, load, loads
import os
from unittest import TestCase
from models.base_model import BaseModel
import json


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

    def test_save_method(self):
        """Test the save() method saved to the JSON file"""
        new_model = BaseModel()
        new_model.name = "Test Model"
        self.storage.new(new_model)
        self.storage.save()

        file_path = self.storage.get_file_path()
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, "r") as file:
            data = json.load(file)

        self.assertIn(new_model.__class__.__name__ + "." + new_model.id, data)
        self.assertEqual(
            data[new_model.__class__.__name__ + "." + new_model.id]["name"],
            "Test Model"
            )

    def test_reload_method(self):
        """Test the reload() method loaded from the JSON file"""
        new_model = BaseModel()
        new_model.name = "Test Model"
        self.storage.new(new_model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn(new_model.__class__.__name__ + "." + new_model.id,
                      new_storage.all())
        reloaded_model = new_storage.all()[new_model.__class__.__name__ + "." +
                                           new_model.id]
        self.assertEqual(reloaded_model.name, "Test Model")
