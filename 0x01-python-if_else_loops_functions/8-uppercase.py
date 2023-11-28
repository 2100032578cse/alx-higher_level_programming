#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            c = chr(ord(ch) - 32)
        else:
            c = ch
        print("{:s}".format(c), end="")
        print()
