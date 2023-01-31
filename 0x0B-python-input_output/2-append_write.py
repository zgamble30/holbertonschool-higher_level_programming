#!/usr/bin/python3
""" 2-append_write.py

    append_write func
"""


def append_write(filename="", text=""):
    """append_write func

    appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str, optional): file. Defaults to "".
        text (str, optional): text. Defaults to "".

    Returns:
        int: number of characters added
    """
    with open(file=filename, mode="a", encoding="utf8") as f:
        f.write(text)

    return len(text)
