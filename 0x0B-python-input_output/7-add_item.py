#!/usr/bin/python3
"""Module 7-add_item with function add_item"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


size = len(sys.argv)
with open("add_item.json", 'a+') as f:
    f.seek(0)
    read_data = f.read()
    if read_data == "":
        json.dump([], f)

new_list = load_from_json_file("add_item.json")
for i in range(1, size):
    new_list.append(sys.argv[i])
save_to_json_file(new_list, "add_item.json")
