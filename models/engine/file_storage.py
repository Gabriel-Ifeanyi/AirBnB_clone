#!/usr/bin/python3
"""
Module that defines the FileStorage class.
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes and deserializes instances to and from JSON files.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets a new object in __objects with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        If the file does not exist, nothing happens.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                loaded_objects = json.load(f)
                for key, value in loaded_objects.items():
                    cls_name, obj_id = key.split('.')
                    obj_dict = value
                    obj_dict['__class__'] = cls_name
                    obj = eval(cls_name + "(**obj_dict)")
                    FileStorage.__objects[key] = obj

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
