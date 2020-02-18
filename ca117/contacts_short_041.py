#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1]) as fd:
        fd = fd.readlines()
    for line in fd:
        line = line.split()
        print(line)



if __name__ == '__main__':
    main()