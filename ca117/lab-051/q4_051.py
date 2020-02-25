#!/usr/bin/env python3

import sys

def mean(l):
    l = sorted(l)
    t = 0
    for i in l:
        t += i
    return t / len(l)

def median(l):
    l = sorted(l)
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[(len(l) // 2) - 1]) / 2
    else:
        return l[len(l) // 2]
def main():
    s = sys.stdin.readlines()
    l = [int(n) for n in s]
    print("Mean: {:.1f}".format(mean(l)))
    print("Median: {:.1f}".format(median(l)))

if __name__ == '__main__':
    main()
