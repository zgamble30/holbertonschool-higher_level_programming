#!/usr/bin/python3
""" 11-student.py

    Student class

    Returns:
        dict: retrieves a dictionary representation
"""


class Student():
    """Student class

    student class with attributes
    """

    def __init__(self, first_name, last_name, age):
        """__init__ constructor

        public attributes for Student class

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json method

        that retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional): is a list of strings. Defaults to None.

        Returns:
            dict: retrieves a dictionary representation
        """
        att = dict()

        if type(attrs) is list and all(isinstance(x, str) for x in attrs):
            for key in attrs:
                if key in self.__dict__.keys():
                    att[key] = self.__dict__[key]
        else:
            att = self.__dict__

        return att

    def reload_from_json(self, json):
        """reload_from_json method

        replaces all attributes of the Student instance

        Args:
            json (dict): will always be a dictionary
        """
        for k, v in json.items():
            if k in self.__dict__.keys():
                self.__dict__[k] = v
