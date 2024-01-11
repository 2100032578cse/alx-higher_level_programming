#!/usr/bin/python3
"""
this is for max int
it will be used to test
"""


def max_integer(list=[]):
    """Func that return max int in list"""
    if len(list) == 0:
        return None
    ans = list[0]
    for i in range(1, len(list)):
        if list[i] > ans:
            ans = list[i]
    return ans
