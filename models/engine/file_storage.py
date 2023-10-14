
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
        """Generates Unique Key Value pair for self.__object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves objects to a JSON file"""
        objects = {}
        for key, value in self.__objects.items():
            objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(objects))

    def reload(self):
        """Deserializes the JSON file into object(s)"""
        objects = {}

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                objects = json.loads(file.read())

            from models.amenity import Amenity
            from models.place import Place
            from models.city import City
            from models.review import Review
            from models.user import User
            from models.state import State
            from models.base_model import BaseModel


            model_classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "Review": Review,
                "Place": Place,
                "City": City,
                "Amenity": Amenity,
        }

            for key, value in objects.items():
                class_name = value.get("__class__", None)
                if class_name:
                    obj_class = model_classes[class_name]
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
                objects = {}

    @classmethod
    def get_file_path(cls):
        return cls.__file_path
