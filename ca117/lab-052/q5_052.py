#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    d = {}
    nd = {}
    skipped = []
    for line in lines:
        line = line.split(":")
        name = line[0]
        line[-1] = line[-1].strip()
        marks = line[1:]
        d[name] = marks
        nd[name] = 0
        print(name)
        for mark in marks:
            if mark.isdigit():
                nd[name] += int(mark)
            else:
                del nd[name]
                skipped.append(name)
    print(nd)
if __name__ == '__main__':
    main()
