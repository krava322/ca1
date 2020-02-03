#!/usr/bin/env python

import sys
args = sys.argv[1:]

i = 0
stars = "*"
b = int(args[0])
spaces = b - 1
while i < b:
    print(spaces * " " + stars)
    i = i + 1
    stars += " *"
    spaces -= 1
stars = stars[0:-4]
spaces = 1
i = 0
while i < b - 1:
    print(spaces * " " + stars)
    i = i + 1
    spaces += 1
    stars = stars[0:-2]
