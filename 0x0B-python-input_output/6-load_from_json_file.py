#!/usr/bin/python3
""" 6-load_from_json_file.py

    load_from_json_file func

    Returns:
        Object: Object from JSON file
"""
import json


def load_from_json_file(filename):
    """load_from_json_file func

    [extended_summary]

    Args:
        filename (file): JSON file

    Returns:
        Object: Object from JSON file
    """
    with open(file=filename, mode="r") as f:
        return json.load(f)
