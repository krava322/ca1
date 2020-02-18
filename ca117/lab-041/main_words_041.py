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
    maxv = 0
    maxk = 0
    for k in sorted(d):
        if k != "" and len(k) > 3 and d[k] >= 3:
            if maxv < len(k):
                maxv = len(k)
            if len(str(d[k])) > maxk:
                maxk = len(str(d[k]))
    for o in sorted(d):
        if o != "" and len(o) > 3 and d[o] >= 3:
            print("{:>{}} : {:{}}".format(o, maxv, d[o], maxk))
if __name__ == '__main__':
    main()
