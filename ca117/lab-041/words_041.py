#!/usr/bin/env python3

import sys
from string import punctuation

def main():
    s = sys.stdin.readlines()
    d = {}
    for i in s:
        i = i.strip().lower().split()
        for j in i:
            for l in j:
                if l in punctuation and l != "'":
                    j = j.replace(l, "")
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
    for k in sorted(d):
        if k != "":
            print(k, ":", d[k])
if __name__ == '__main__':
    main()
