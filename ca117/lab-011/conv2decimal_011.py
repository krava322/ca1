#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readlines()
    for i in s:
        b = i.split(" ")
        b[1] = b[1].strip()
        power = len(b[0]) - 1
        summ = 0
        for j in b[0]:
            summ += int(j) * int(b[1]) ** power
            power -= 1
        print(summ)
        summ = 0
if __name__ == "__main__":
   main()
