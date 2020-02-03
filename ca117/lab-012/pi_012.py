#!/usr/bin/env python3

import sys
import math
args = sys.argv[1:]
def main():
    j = int(args[0])
    print("{:.{}f}".format(math.pi, j))
if __name__ == '__main__':
    main()
