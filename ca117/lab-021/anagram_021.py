#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        [s1, s2] = line.split()
        if sorted(s1) == sorted(s2):
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    main()
