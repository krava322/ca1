#!/usr/bin/env python3

import sys

def main():
    file_name = sys.argv[1]
    try:
        with open(file_name) as fd:
            fd = fd.readlines()
        for i in fd:
            i = i.split()
            i[0] = int(i[0])
    except(ValueError):
        print("Invalid mark " + i[0] + " encountered. Exiting.")
if __name__ == '__main__':
    main()
