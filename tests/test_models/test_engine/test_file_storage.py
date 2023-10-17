#!/usr/bin/python3
"""
Define Test Class of FileStorage class
"""
from models.engine.file_storage import FileStorage
import os
from unittest import TestCase
from models.base_model import BaseModel
from models.user import User
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
        super().setUp()
        self.storage = FileStorage()
        self.storage.reload()

    def test_new(self):
        """Test if new function adds an object to __objects"""
        new_model = BaseModel()
        self.storage.new(new_model)
        key = f"{new_model.__class__.__name__}.{new_model.id}"
        self.assertIn(key, self.storage.all())

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
        objects = {key: value.to_dict()
                   for key, value in self.storage.storage_objs.items()}
        self.assertEqual(objects, data)

    def test_reload_method(self):
        """Test the reload() method loaded from the JSON file"""
        storage = FileStorage()

        self.assertEqual(storage.all(), {})

        new_model = BaseModel()
        new_model.name = "Test Model"
        storage.new(new_model)
        storage.save()

        storage.reload()

        user_model = User()
        user_model.email = "roman@email.com"
        storage.new(user_model)
        storage.save()

        storage.reload()

#        new_storage = FileStorage()
#        new_storage.reload()

        key = f"{type(user_model).__name__}.{user_model.id}"

        self.assertEqual(user_model.to_dict(), storage.all()[key].to_dict())

        file_path = storage.get_file_path()
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, "r") as file:
            data = json.load(file)

        self.assertIn(new_model.__class__.__name__ + "." + new_model.id,
                      storage.all())
        reloaded_model = storage.all()[new_model.__class__.__name__ +
                                       "." + new_model.id]
        self.assertEqual(reloaded_model.name, "Test Model")

        objects = {key: value.to_dict()
                   for key, value in storage.all().items()}
        self.assertEqual(objects, data)
