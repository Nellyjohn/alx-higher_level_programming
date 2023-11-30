#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    for arg in range(len(argv) - 1):
        result += int(argv[arg + 1])
    print("{}".format(result))
