#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = len(argv) - 1
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args))
    for i in range(args):
        print("{}: {}".format(i + 1, argv[i + 1]))
