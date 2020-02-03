#!/usr/bin/env python3

import sys

def main():
  s = sys.stdin.readlines()
  for i in s:
    b = i.split(" ")
    b[0].lower()
    b[1].lower().strip()
    for j in b[0]:
      if j in b[1]:
        b[1] = b[1].replace(j, "")
      elif j not in b[0]:
        print(False)
        break
    if len(b[1]) == 0:
      print(True)
if __name__ == "__main__":
  main()
