#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding = 'utf-8') as fl:
        for a in fl:
            print(a, end="")
    fl.close()
