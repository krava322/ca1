#!/usr/bin/env python3

import sys
import math

def main():
    s = sys.stdin.readlines()
    for i in s:
        print("{:^s}".format(i.strip()))

if __name__ == '__main__':
    main()
