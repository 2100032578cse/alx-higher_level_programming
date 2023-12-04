#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    n = len(sentence)
    if n != 0:
        tup = n, sentence[0]
    else:
        tup = 0, "None"
    return tup
