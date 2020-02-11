#!/usr/bin/env python3

import sys
def main():
    n = sys.argv[1]
    a = [x if x % 3 != 0 and x != 0 else "X" for x in range(int(n) + 1)]

    print("Multiples of 3:", [x for x in range(int(n) + 1) if x % 3 == 0 and x != 0])
    print("Multiples of 3 squared:", [x * x for x in range(int(n) + 1) if x % 3 == 0 and x != 0])
    print("Multiples of 4 doubled:", [x * 2 for x in range(int(n) + 1) if x % 4 == 0 and x != 0])
    print("Multiples of 3 or 4:", [x for x in range(int(n) + 1) if x % 3 == 0 and x != 0 or x % 4 == 0 and x != 0])
    print("Multiples of 3 and 4:", [x for x in range(int(n) + 1) if x % 3 == 0 and x % 4 == 0 and x != 0])
    print("Multiples of 3 replaced:", a[1:])
    print("Primes:", [p for p in range(2, int(n)) if 0 not in [p % d for d in range(2, p)]])
if __name__ == '__main__':
    main()
