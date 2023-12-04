#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    i = 0
    if n > 0:
        my_list.reverse()
        while i < n:
            print("{:d}".format(my_list[i]))
            i += 1
