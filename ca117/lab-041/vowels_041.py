#!/usr/bin/env python3

import sys
from string import punctuation

def main():
    s = sys.stdin.readlines()
    d = {}
    vow = "eaoiu"
    for i in s:
        i = i.strip().lower().split()
        for j in i:
            for l in j:
                if l in vow and l not in d:
                    d[l] = 1
                elif l in vow:
                    d[l] += 1
    maxk = 0
    for k in sorted(d):
        if len(str(d[k])) > maxk:
            maxk = len(str(d[k]))
    ansl = []
    for i in sorted(d, key=d.get):
        ansl.append("{} : {:>{}}".format(i, d[i], maxk))
    i = 0
    j = -1
    while i < len(ansl):
        print(ansl[j])
        i += 1
        j -= 1

if __name__ == '__main__':
    main()
