#!/usr/bin/env python3

'''Demonstrate use of extract_range function.'''

import sys

def build_dictionary(filename):
    d = {}
    with open(filename) as fd:
        fd = fd.readlines()
    for line in fd:
        line = line.split()
        d[line[0]] = int(line[1])
    return d
def extract_range(d, low, high):
    nd = {}
    for key in d:
        if d[key] >= low and d[key] <= high:
            nd[key] = d[key]
    return nd

def main():
    d = build_dictionary('q3_052_mappings.txt')

    nd = extract_range(d, 5, 15)

    for (k, v) in sorted(nd.items()):
        print('{} : {}'.format(k, v))

if __name__ == '__main__':
    main()
