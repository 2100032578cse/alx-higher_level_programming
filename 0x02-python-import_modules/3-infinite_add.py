#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    leng = len(argv)
    ans = 0
    for i in range(1, leng):
        ans = ans + int(argv[i])
print(ans)
