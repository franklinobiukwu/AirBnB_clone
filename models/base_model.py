#!/usr/bin/python3
"""BaseModel Class Module"""
import uuid
import datetime


class BaseModel:
    """BaseModel class that defines all common attributes for other clases"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()


    def __str__(self):
        """Return string representation of instance of class"""
        return f"{[self.__class__.__name__]} ({(self.id)}) {self.__dict__}"

    def save(self):
        """Updates public instance attribute of updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dict containing key value pairs of instances"""
        dict = {}
        for key, value in self.__dict__.items():
            dict[key] = value
            if key == "created_at":
                dict[key] = value.isoformat()
            if key == "updated_at":
                dict[key] = value.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict
