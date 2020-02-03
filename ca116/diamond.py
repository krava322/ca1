#!/usr/bin/env python

import sys
args = sys.argv[1:]

i = 0
stars = 1
b = int(args[0])
while i < b / 2:
  print (b - stars) / 2 * " " + stars * "*"
  i = i + 1
  stars = stars + 2
print (b - stars) / 2 * " " + stars * "*"
stars = stars - 2
i = 0
while i < b / 2:
  print (b - stars) / 2 * " " + stars * "*"
  i = i + 1
  stars = stars - 2
