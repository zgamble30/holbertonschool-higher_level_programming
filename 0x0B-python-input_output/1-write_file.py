#!/usr/bin/python3
""" 1-write_file.py

    write_file func
"""


def write_file(filename="", text=""):
    """write_file func

    writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str, optional): file. Defaults to "".
        text (str, optional): text for writing. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(file=filename, mode="w", encoding="utf8") as f:
        f.write(text)

    return len(text)
