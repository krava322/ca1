#!/usr/bin/env python3

import sys

def calories(filename):
    cald = {}
    with open(filename) as fd:
        fd = fd.readlines()
    for line in fd:
        line = line.rsplit(" ", 1)
        cald[line[0]] = int(line[1])
    return cald
def longestk(d):
    longestk = 0
    for k in d:
        if len(k) > longestk:
            longestk = len(k)
    return longestk

def longestv(d):
    longestv = 0
    for v in d:
        if len(str(d[v])) > longestv:
            longestv = len(str(d[v]))
    return longestv

def main():
    lines = sys.stdin.readlines()
    d = {}
    cald = calories(sys.argv[1])
    finald = {}
    for line in lines:
        line = line.split(",")
        line[-1] = line[-1].strip()
        name = line[0]
        foods = line[1:]
        d[name] = foods
        finald[name] = 0
        for v in d[name]:
            if v in cald:
                finald[name] += cald[v]
            else:
                finald[name] += 100
    sorted_d = sorted((v, k) for (k, v) in finald.items())
    for i in sorted_d:
        print("{:>{}s} : {:{}d}".format(i[1], longestk(finald), i[0], longestv(finald)))
if __name__ == '__main__':
    main()
