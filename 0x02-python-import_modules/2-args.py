#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
   leng = len(argv) - 1
      if leng == 0:
        print("{} arguments.".format(leng))
      else:
          if leng == 1:
              print("{} argument:".format(leng))
          else:
              print("{} arguments:".format(leng))
        i = 1
        while(i <= leng):
            print("{}: {}".format(i, argv[i]))
            i += 1
