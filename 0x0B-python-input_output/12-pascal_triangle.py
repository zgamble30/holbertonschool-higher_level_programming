i#!/usr/bin/python3
""" 12-pascal_triangle.py

    pascal_triangle func
"""


def pascal_triangle(n):
    """pascal_triangle func

    returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n (int): number of list

    Returns:
        list: pascal's triangle matrix
    """
    pascal = list()

    if n <= 0:
        return pascal

    pascal = [[1]]
    for i in range(1, n):
        tmp = []
        for j in range(i+1):
            if(j == 0):
                tmp.append(1)
                continue
            elif(j == i):
                tmp.append(1)
                continue
            else:
                tmp.append(pascal[i-1][j]+pascal[i-1][j-1])
        pascal.append(tmp)

    return pascal
