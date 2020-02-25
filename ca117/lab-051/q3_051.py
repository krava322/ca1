#!/usr/bin/env python3

import sys

def swapper(l):
    if l.isupper():
        return l
    else:
        return "0"

def main():
    lines = sys.stdin.readlines()
    for word in lines:
        word = word.strip()
        a = [swapper(l) for l in word]
        string = "".join(a)
        string = string.split("0")
        print(max(string, key=len))
if __name__ == '__main__':
    main()
