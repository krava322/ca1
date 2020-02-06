#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readlines()
    for i in s:
        i = i.strip()
        if i.isdigit():
            print("Thank you for " + i)
            break
        else:
            print(i + " is not a number")

if __name__ == '__main__':
    main()
