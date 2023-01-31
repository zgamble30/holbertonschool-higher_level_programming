#!/usr/bin/python3
"""Module 5-base_geometry with class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry with public method
        area(): raises an exception saying area is not implemented
        integer_validator(): checks if value is an integer
    """
    def area(self):
        """Method area that needs to be implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an int
            name: name of value
            value: value to check if int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
