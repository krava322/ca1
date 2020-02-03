#!/usr/bin/env python3

import sys
import math

def main():
    s = sys.stdin.readlines()
    maxl = len(s[0].strip())
    for k in s:
        k = k.strip()
        if len(k.strip()) > maxl:
            maxl = len(k.strip())
    for i in s:
        print("{:^{}s}".format(i.strip(), maxl))

if __name__ == '__main__':
    main()
