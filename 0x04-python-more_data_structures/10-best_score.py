#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        ans = max(a_dictionary, key=a_dictionary.get)
        return ans
    return None
