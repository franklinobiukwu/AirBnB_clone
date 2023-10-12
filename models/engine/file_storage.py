#!/usr/bin/python3
"""FileStorage Class Module"""
from json import loads, dumps, load, dump
import os


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
#        print(FileStorage.__objects)
        
    def save(self):
        """Saves object to json file"""
        new_dict = {}
        
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        print(new_dict)     
        with open(FileStorage.__file_path, "w") as file:
            dump(new_dict, file)
    
    def reload(self):
        """Reload a string into a dict"""
        object = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                object = loads(file.read())
            from models.base_model import BaseModel
            for key, value in object.items():
                class_name = value["__class__"]
                del(value["__class__"])
                if class_name == "BaseModel":
                    obj = BaseModel(**value)
                    object[key] = obj
                
        FileStorage.__objects = object
                
            
            
                
        
        
