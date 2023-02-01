#!/usr/bin/python3
#task0
""" 0-read_file.py

    read_file func
"""


def read_file(filename=""):
    """read_file func

    reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): file. Defaults to "".
    """
    with open(file=filename, mode="r", encoding="utf8") as f:
        for line in f:
            print(line, end="")
