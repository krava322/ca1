#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    t = 0
    for line in lines:
        line = line.split()
        t += len(line)
    print(t)
if __name__ == '__main__':
    main()
