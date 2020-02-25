#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    pair1 = 1
    pair2 = 0
    ans = ""
    while pair1 < len(s):
            ans += s[pair1] + s[pair2]
            pair2 += 2
            pair1 += 2
    if len(s) % 2 == 1:
        ans += s[-1]
    print(ans)

if __name__ == '__main__':
    main()
