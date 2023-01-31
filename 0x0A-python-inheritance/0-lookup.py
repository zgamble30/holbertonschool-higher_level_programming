#!/usr/bin/python3
"""Module for 0-lookup with function lookup()"""


def lookup(obj):
    """function lookup - looks up attributes adn methods
        obj: object to lookup
        Return: list of attributes and methods
    """
    return dir(obj)