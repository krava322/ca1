#!/usr/bin/env python3

import sys

def main():
    word = sys.argv[1]
    number = int(sys.argv[2])
    while number >= len(word):
        number -= len(word)
    front = word[:-1 * number]
    back = word[-number:]
    print(back + front)

if __name__ == '__main__':
    main()
