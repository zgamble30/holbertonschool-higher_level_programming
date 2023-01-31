#!/usr/bin/python3
"""Module 3-is_kind_of_class including function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Function is_kind_of_class - checks obj with a_class
        obj: object to check type
        a_class: class to check with obj
        Return: True if instance of a_class or False
    """

    return isinstance(obj, a_class)
