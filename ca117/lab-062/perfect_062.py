#!/usr/bin/env python3

import sys

def sumFac(n):
    sumfac = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sumfac += i
    return sumfac

def isPerfect(n):
    if n == sumFac(n):
        return True
    return False

def main():
    inp = sys.stdin.readlines()
    for number in inp:
        number = int(number.strip())
        print(isPerfect(number))


if __name__ == '__main__':
    main()
