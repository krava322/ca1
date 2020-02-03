#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readlines()
    for i in s:
        b = i.split("@")
        k = b[0].split(".")
        k[1] = k[1].strip()
        q = 0
        while q < len(k[1].strip()):
            if k[1][q] <= "0" or k[1][q] >= "9":
                q += 1
            else:
                break
        print(k[0].capitalize(), k[1][0:q].capitalize())
if __name__ == "__main__":
   main()
