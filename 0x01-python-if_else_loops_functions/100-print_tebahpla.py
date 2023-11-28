#!/usr/bin/python3
for i in range(123, 96, -2):
        print("{:c}{:s}".format(i, chr(i - 33)), end="")
