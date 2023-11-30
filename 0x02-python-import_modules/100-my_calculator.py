#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    leng = len(argv) - 1
    if leng != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        ops = argv[2]
        if not (ops == '+' or ops == '-' or ops == '*' or ops == '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        a = int(argv[1])
        b = int(argv[3])
        addition = add(a, b)
        mult = mul(a, b)
        subt = sub(a, b)
        divs = div(a, b)
        if ops == '+':
            print("{} + {} = {}".format(a, b, addition))
        if ops == '-':
            print("{} - {} = {}".format(a, b, subt))
        if ops == '*':
            print("{} * {} = {}".format(a, b, mult))
        if ops == '/':
            print("{} / {} = {}".format(a, b, divs))
