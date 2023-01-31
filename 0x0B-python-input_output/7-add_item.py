#!/usr/bin/python3
""" 7-add_item.py

    adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    for item in sys.argv[1::]:
        items.append(item)

    save_to_json_file(items, filename)
