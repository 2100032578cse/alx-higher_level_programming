#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    leng = len(argv) - 1
    if leng == 1:
        print('0 arguments.')
    elif leng == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(leng - 1))
        while i < leng:
            print("{:d}{:s}".format(i, argv[i]))
            i = i + 1
