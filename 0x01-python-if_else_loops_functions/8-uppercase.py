#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            c = chr(ord(ch) - 32)
        else:
            c = ch
        print("{:s}".format(c), end="")
        print()
