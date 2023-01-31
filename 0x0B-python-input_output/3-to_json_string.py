#!/usr/bin/python3
""" 3-to_json_string.py

    to_json_string func

    Returns:
        str: JSON representation
"""
import json


def to_json_string(my_obj):
    """to_json_string func

    returns the JSON representation of an object (string)

    Args:
        my_obj (JSON): JSON object

    Returns:
        str: JSON representation
    """
    return str(json.JSONEncoder().encode(my_obj))
