#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a >= b:
        return (sub(a, b))
    else:
        ans = add(a, b)
        for i in range(4, 6):
            ans = add(ans, i)
        return (ans)
