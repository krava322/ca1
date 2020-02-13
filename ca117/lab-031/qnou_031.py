#!/usr/bin/env python3

import sys

def qnou(string):
    string = string.lower().replace("qu", "--")
    return "q" in string

def main():
    l = []
    s = sys.stdin.readlines()
    for i in s:
        l.append(i.strip())
    k = [x for x in l if qnou(x) is True]
    print("Words with q but no u: " + str(k))

if __name__ == '__main__':
    main()
