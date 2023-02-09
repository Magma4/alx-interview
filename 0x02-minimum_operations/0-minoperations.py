#!/usr/bin/python3

"""
A method that calculates the fewest number of operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Prototype: def minOperations(n)
    Returns an integer If n is impossible to achieve, return 0
    """
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
