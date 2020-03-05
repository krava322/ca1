#!/usr/bin/env python3

import sys
from math import sqrt

def roots(a, b, c):
    root = (b ** 2) - 4 * a * c
    bottom = 2 * a
    if root >= 0 and bottom != 0:
        ans1 = (-b + sqrt(root)) / bottom
        ans2 = (-b - sqrt(root)) / bottom
        return "r1 = " + str(ans1) + ", " + "r2 = " + str(ans2)

def main():
    nums = sys.stdin.readlines()
    for numbers in nums:
        a, b, c = numbers.split()
        x = roots(int(a), int(b), int(c))
        print(x)

if __name__ == '__main__':
    main()
