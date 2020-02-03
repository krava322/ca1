#!/usr/bin/env python3

import sys
def cap(s):
  return s.capitalise()

def main():
  k = sys.stdin.readlines()
  for line in k:
    print(cap(line))
if __name__ == "__main__":
  main()
