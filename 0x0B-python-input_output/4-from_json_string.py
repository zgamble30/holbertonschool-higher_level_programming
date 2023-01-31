#!/usr/bin/python3
""" 4-from_json_string.py

    from_json_string func

    Returns:
        JSON: object (Python data structure)
"""
import json


def from_json_string(my_str):
    """from_json_string [summary]

    returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (JSON str): JSON string

    Returns:
        JSON: object (Python data structure)
    """
    return json.loads(my_str)
