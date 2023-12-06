#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = len(my_list)
    nlist = []
    for i in range(n):
        if my_list[i] == search:
            nlist.append(replace)
        else:
            nlist.append(my_list[i])
    return nlist
