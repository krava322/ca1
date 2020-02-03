#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readlines()
    for i in s:
        b = i.split(" ")
        ans = ""
        for j in b:
            j = j.strip()
            k = j[len(j) - 1]
            ans += j[0:len(j) - 1] + k.capitalize() + " "
        print(ans[0:len(ans) - 1])
if __name__ == "__main__":
   main()
