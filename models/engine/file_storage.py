#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from json.decoder import JSONDecodeError


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {key: val for key, val in FileStorage.__objects.items()
                    if key.startswith(cls.__name__)}
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        dictionary = self.all()
        dictionary[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        cls = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                json_str = f.read()
                temp = json.loads(json_str)
                for key, val in temp.items():
                    FileStorage.__objects[key] = cls[val['__class__']](**val)
        except FileNotFoundError:
            pass
        except JSONDecodeError as e:
            print(f"Err decoding JSON in file {FileStorage.__file_path}: {e}")
            print("Problematic JSON string:")
            print(json_str)

    def delete(self, obj=None):
        """Deletes the specified object"""
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """Calls the `reload()` method"""
        reload()
