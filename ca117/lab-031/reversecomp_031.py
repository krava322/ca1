#!/usr/bin/env python3

import sys

def rev(k):
   valid = {word.lower(): True for word in k if len(word) >= 5}
   k = [word for word in k if word.lower()[::-1] in valid]
   print(k)
   return k

def main():
   k = [word.strip() for word in sys.stdin]
   rev(k)

if __name__ == "__main__":
    main()
