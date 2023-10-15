#!/usr/bin/python3
"""
Define Test Class of FileStorage class
"""
from models.engine.file_storage import FileStorage
from json import dump, dumps, load, loads
import os
from unittest import TestCase


class TestFileStorage(TestCase):
    """
    Test Class for the File Storage class
    """
