#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1]) as fd:
        fd = fd.readlines()
    d = {}
    for line in fd:
        line = line.split()
        d[line[0]] = line[1]
    names = sys.stdin.readlines()
    for name in names:
        name = name.strip()
        if name in d:
            print("Name:", name)
            print("Phone:", d[name])
        else:
            print("Name:", name)
            print("No such contact")

if __name__ == '__main__':
    main()
