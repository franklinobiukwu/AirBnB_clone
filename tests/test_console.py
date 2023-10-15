#!/usr/bin/python3
"""
Defines the Command Interpreter class
"""
from unittest import TestCase
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User
from models.state import State


class TestConsole(TestCase):
    """
    Defines Test Class for Console Tests
    """
    pass
