#!/usr/bin/python3
def uniq_add(my_list=[]):
    #n = len(set(my_list))
    res = 0
    newlist = set(my_list)
    for i in newlist:
        res = res + i
    return res
