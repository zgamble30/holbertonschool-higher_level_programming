#!/usr/bin/python3
""" 8-class_to_json.py

    class_to_json func
"""


def class_to_json(obj):
    """class_to_json func

    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (object): is an instance of a Class

    Returns:
        dict: the dictionary description with simple data structure
    """
    return obj.__dict__
