#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.read().split()
    d = {}
    for word in lines:
        new = ""
        for letter in word:
            if letter.isalnum():
                new += letter
        if new != "":
            new = new.lower()
        if new not in d:
            d[new] = True
    print(len(d) - 1)
if __name__ == '__main__':
    main()
