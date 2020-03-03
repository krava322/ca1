#!/usr/bin/env python3

import sys

def main():
    word = sys.argv[1]
    number = int(sys.argv[2])
    part1 = number // len(word)
    print(part1)


if __name__ == '__main__':
    main()
