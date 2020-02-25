#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    letters = "evil"
    for word in lines:
        dublicate = word.strip()
        word = word.strip().lower()
        a = [l for l in word if l in letters]
        if "".join(a) == letters:
            print(dublicate)

if __name__ == '__main__':
    main()
