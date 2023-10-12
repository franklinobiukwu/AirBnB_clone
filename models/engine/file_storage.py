#!/usr/bin/python3
"""FileStorage Class Module"""
import json
import os



class FileStorage:
    """ FileStorage class that save and reloads to JSON file"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    def save(self):
        """Saves object to json file"""
        new_dict = {}
        
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
            
        with open(FileStorage.__file_path, "w") as file:
            json.dumps(new_dict,file)
    
    def reload(self):
        """Reload a string into a dict"""
        second_dict={}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                second_dict = json.loads(file.read())
        
        
