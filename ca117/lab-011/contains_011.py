#!/usr/bin/env python3

import sys

def main():
  s = sys.stdin.readlines()
  for i in s:
    b = i.split(" ")
    b[0].lower()
    b[1].lower().strip()
    c = 0
    k = 0
    for j in b[0].lower():
      if j in b[1].lower():
        b[1] = b[1].replace(j, "", k)
        b[0] = b[0].replace(j, "", 0)
        k += 1
      else:
        print(False)
        c = 1
        break
    if c != 1:
      print(True)

if __name__ == "__main__":
  main()
