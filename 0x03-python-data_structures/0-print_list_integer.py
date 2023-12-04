#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list)
    i = 0
    while i < n:
        print("{:d}".format(my_list[i]))
        i += 1
