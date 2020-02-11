#!/usr/bin/env python3

import sys

def main():
    s = sys.stdin.readlines()
    r = "qu"
    k = [x.strip() for x in s if r not in x.lower().strip()]
    print("Words with q but no u:", k)

if __name__ == '__main__':
    main()
