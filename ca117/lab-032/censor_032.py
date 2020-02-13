#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1]) as ff:
        ff = ff.readlines()
    s = sys.stdin.read()
    for bword in ff:
        bword = bword.strip().lower()
        if bword in s:
            s = s.replace(bword, len(bword) * "@")
    print(s[:-1])

if __name__ == "__main__":
    main()
