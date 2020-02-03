#!/usr/bin/env python3

import sys

def main():
  passw = sys.stdin.readlines()
  t = 0
  for i in passw:
    digit = 0
    lower = 0
    upper = 0
    other = 0
    for j in i.strip():
      if j.isdigit():
        digit = 1
      elif j.islower():
        lower = 1
      elif j.isupper():
        upper = 1
      else:
        other = 1
    print(digit + lower + upper + other)

if __name__ == "__main__":
  main()
