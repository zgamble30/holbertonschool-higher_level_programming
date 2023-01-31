#!/usr/bin/python3
""" 9-student.py

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

    def to_json(self):
        """to_json method

        retrieves a dictionary representation of a Student instance

        Returns:
            dict: retrieves a dictionary representation
        """
        return self.__dict__
