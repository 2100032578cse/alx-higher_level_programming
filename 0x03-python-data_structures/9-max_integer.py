#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    i = 0
    if n != 0:
        mx = my_list[0]
        while i < n:
            if (my_list[i]) > mx:
                mx = my_list[i]
            i = i + 1
        return mx
    else:
        return "None"
