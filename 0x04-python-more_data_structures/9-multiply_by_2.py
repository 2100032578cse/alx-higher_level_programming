#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictnew = a_dictionary.copy()
    for i in a_dictionary.keys():
        dictnew[i]= a_dictionary[i] * 2
    return dictnew
