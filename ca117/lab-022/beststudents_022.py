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
            except (ValueError):
                print("Invalid mark " + i[0] + " encountered. Skipping.")
        for k in fd:
            k = k.split()
            if str(maxv) in k:
                name += " ".join(k[1:]) + ", "
        print("Best student(s): " + name[:-2])
        print("Best mark: " + str(maxv))
    except (FileNotFoundError):
        print("The file " + file_name + " could not be oppened.")

if __name__ == '__main__':
    main()
