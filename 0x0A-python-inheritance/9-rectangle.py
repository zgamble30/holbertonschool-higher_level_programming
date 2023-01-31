#!/usr/bin/python3
""" 9-rectangle.py

    Rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle func

    Rectangle that inherits from BaseGeometry

    Args:
        BaseGeometry: base class
    """

    def __init__(self, width, height):
        """__init__ contructor

        Constructor Rectangle

        Args:
            width (integer): width rectangle
            height (integer): height rectangle
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """area method

        Area of Rectangle

        Returns:
            integer: area
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__ method

        string class

        Returns:
            string: representation
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
