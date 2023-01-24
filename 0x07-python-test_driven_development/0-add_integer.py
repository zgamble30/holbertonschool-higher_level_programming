#!/usr/bin/python3
"""Module 0-add_integer
    contains add_integer function
"""


def add_integer(a, b=98):
    """Function add_integer takes in at-least one int or float arg
        a: can be a float or int
        b: can be a float or int or not even given
        Return: the sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
