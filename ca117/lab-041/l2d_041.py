#!/usr/bin/env python3

import sys

def l2d(d):
    s = sys.stdin.readlines()
    d = {}
    s[0] = s[0].split()
    s[1] = s[1].split()
    i = 0
    while i < len(s[0]):
        d[s[0][i]] = s[1][i]
        i += 1
    return d

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print("{} : {}".format(k, v))

if __name__ == '__main__':
    main()
