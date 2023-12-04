#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    og = my_list.copy()
    if (idx < 0):
        return og
    elif (idx >= len(my_list)):
        return og
    else:
        og[idx] = element
        return og
