#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    letters = "aeiou"
    for word in lines:
        dub = word.strip()
        word = word.strip().lower()
        a = [l for l in word if l in letters]
        if "".join(a) == letters:
            print(dub)

if __name__ == '__main__':
    main()
