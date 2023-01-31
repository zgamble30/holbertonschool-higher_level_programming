i#!/usr/bin/python3
"""5-save_to_json_file.py

    save_to_json_file func
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file func

    writes an Object to a text file, using a JSON representation

    Args:
        my_obj (object): object
        filename (FILE): file
    """
    with open(file=filename, mode="w") as f:
        f.write(json.dumps(my_obj))
