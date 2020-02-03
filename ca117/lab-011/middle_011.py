#!/usr/bin/env python3

import sys

def main():
   s = sys.stdin.readlines()
   for i in s:
      i = i.strip()
      if len(i) % 2 == 1:
         print(i[len(i) // 2])
      else:
         print("No middle character!")
if __name__ == "__main__":
   main()
