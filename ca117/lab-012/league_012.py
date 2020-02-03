#!/usr/bin/env python3

import sys
import math

def main():
    s = sys.stdin.readlines()
    h1 = 'POS'
    h2 = "CLUB"
    h3 = 'P'
    h4 = "W"
    h5 = "D"
    h6 = "L"
    h7 = "GF"
    h8 = "GA"
    h9 = "GD"
    h10 = "PTS"
    maxclub = 0
    for i in s:
        k = i.split(" ")
        cur = 0
        for j in k:
            if j[0].isupper():
                cur += (len(j))
                if cur > maxclub:
                    maxclub = cur

    for r in s:
        r = r.split(" ")
        if len(r) == 10:
            h1 = r[0]
            h2 = r[1]
            h3 = r[2]
            h4 = r[3]
            h5 = r[4]
            h6 = r[5]
            h7 = r[6]
            h8 = r[7]
            h9 = r[8]
            h10 = r[9].strip()
        elif len(r) == 11:
            h1 = r[0]
            h2 = r[1] + " " + r[2]
            h3 = r[3]
            h4 = r[4]
            h5 = r[5]
            h6 = r[6]
            h7 = r[7]
            h8 = r[8]
            h9 = r[9]
            h10 = r[10].strip()
        elif len(r) == 12:
            h1 = r[0]
            h2 = r[1] + " " + r[2] + " " + r[3]
            h3 = r[4]
            h4 = r[5]
            h5 = r[6]
            h6 = r[7]
            h7 = r[8]
            h8 = r[9]
            h9 = r[10]
            h10 = r[11].strip()
        print('{:>2s} {:>{}s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, maxclub, h3, h4, h5, h6, h7, h8, h9, h10))

if __name__ == '__main__':
    main()
