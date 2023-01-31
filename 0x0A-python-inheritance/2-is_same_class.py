#!/usr/bin/python3
""" 2-is_same_class.py

    is_same_class func
"""


def is_same_class(obj, a_class):
    """is_same_class func

    returns True if the object is exactly an instance
    of the specified class ; otherwise False.

    Args:
        obj (Any): object
        a_class (Any): class

    Returns:
        Boolean: True or False
    """
    if type(obj) is not a_class:
        return False

    return True
