#!/usr/bin/env python3

import sys

def main():
    file_name = sys.argv[1]
    try:
        with open(file_name) as fd:
            fd = fd.readlines()
        maxv = 0
        name = ""
        for i in fd:
            i = i.split()
            try:
                if int(i[0]) > maxv:
                    maxv = int(i[0])
                    name = " ".join(i[1:])
            except (ValueError):
                print("Invalid mark " + i[0] + " encountered. Skipping.")
        print("Best student: " + name)
        print("Best mark: " + str(maxv))
    except (FileNotFoundError):
        print("The file " + file_name + " could not be oppened.")

if __name__ == '__main__':
    main()
