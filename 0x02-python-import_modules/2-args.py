#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    leng = len(argv)
    if leng == 1:
        print('0 arguments.')
    elif leng == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print('{} arguments:'.format(leng - 1))
        i  = 1
        while i < leng:
            print("{}{}".format(i,argv[i]))
            i = i + 1

