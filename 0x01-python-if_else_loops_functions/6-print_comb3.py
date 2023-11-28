#!/usr/bin/python3
for i in range (0, 90):
    rem = i % 10
    div = i / 10
    if rem > div:
        if i == 89:
            print("{:02d}".format(i))
        else:
            print("{:02d}".format(i), end=", ")
