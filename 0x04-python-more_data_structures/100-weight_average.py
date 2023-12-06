#!/usr/bin/python3
def weight_average(my_list=[]):
    n = 0
    d = 0
    if len(my_list) == 0:
        return 0
    for tup in my_list:
        n = n + tup[0] * tup[1]
        d = d + tup[1]
    ans = n / d
    return ans
