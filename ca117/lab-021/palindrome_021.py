#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.lower()
        new = ""
        for k in line:
            if k.isalnum():
                new += k
        if new == new[::-1]:
            print(True)
        else:
            print(False)
if __name__ == '__main__':
    main()
