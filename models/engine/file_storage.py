
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
        self.__objects[key] = obj.to_dict_no_class()
#        print("PRINT OBJ BELOW")  # test line -> delete
#        print(self.__objects)  # test line -> delete

    def save(self):
        """Saves object to json file"""
        # Serialize __object to json file
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Reload a string into a dict"""
        # deserialize JSON file to __object
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        else:
            return

    @classmethod
    def get_file_path(cls):
        return cls.__file_path
