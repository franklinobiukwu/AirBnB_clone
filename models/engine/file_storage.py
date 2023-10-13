#!/usr/bin/python3
"""FileStorage Class Module"""
from json import loads, dumps, load, dump
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """ FileStorage class that save and reloads to JSON file"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

        
    def save(self):
        """Saves object to json file"""
        new_dict = {}
        
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            dump(new_dict, file)
    
    def reload(self):
        """Reload a string into a dict"""

        class_mappings = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review
        }
        
        loaded_objects = {}
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                object = loads(file.read())
            
            for key, value in object.items():
                class_name = value.pop("__class__", None)
                if class_name and class_name in class_mappings:
                    obj_class = class_mappings[class_name]
                    obj = obj_class(**value)
                    loaded_objects[key] = obj

        FileStorage.__objects = loaded_objects

     
                
            
            
                
        
        
