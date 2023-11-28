#!/usr/bin/python3
for i in reversed(range(97, 123)):
        print("{:c}{:s}".format(i, chr(i - 33)), end="")
