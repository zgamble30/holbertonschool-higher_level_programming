#!/usr/bin/python3
"""Module 4-inherits_from with function inherits_from
"""


def inherits_from(obj, a_class):
    """Function inherits_from
        obj: object to check
        a_class: parent class
        Return True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
