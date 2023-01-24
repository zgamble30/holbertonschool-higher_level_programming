#!/usr/bin/python3
""" 0-add_integer

   add_integer function
"""


def add_integer(a, b=98):
    """add integer function

    Args:
        a: first integer
        b: second integer

    Raise:
        TypeError: a must be an integer
        Typeerror: b must be an integer

    Returns:
        sum of two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)

    return a + b
