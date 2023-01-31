#!/usr/bin/python3
"""Module models.base with base class"""


from os import path
import json


class Base:
    """Class Base that instanciates with id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instanciate with id if present"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to get JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of object's dictionary representation to a file"""
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_dict = obj.to_dictionary()
                json_list.append(json_dict)
        json_string = Base.to_json_string(json_list)
        filename = cls.__name__ + ".json"
        with open(filename, 'w+') as f:
            data = f.read()
            f.seek(0)
            f.write(json_string)
            f.truncate()

    @classmethod
    def create(cls, **dictionary):
        """Creates a new object with given dict"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """loads a json object form a file"""
        filename = cls.__name__ + ".json"
        list_dict = []
        if not path.exists(filename):
            return list_dict
        with open(filename, 'r') as f:
            list_dict = json.load(f)
            cls.from_json_string(cls.to_json_string(list_dict))
        list_obj = []
        for dic in list_dict:
            list_obj.append(cls.create(**dic))
        return list_obj
