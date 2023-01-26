#!/usr/bin/python3
"""
Interview question about the Pascal Triangle
Returns a list of integers repping the pascal triangle
"""


def pascal_triangle(n):
    """
    This function returns a lsit of lists of integers.
    representing pascal's triangle with n.
    """

    arr = [[] for i in range(n)]
    if n <= 0:
        return []

    for i in range(n):
        for p in range(i + 1):
            if p == 0 or p == i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i - 1][p - 1] + arr[i - 1][p])
    return arr