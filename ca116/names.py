#!/usr/bin/env python

import sys
filename = "boys.txt"
filename2 = "girls.txt"
d = {}

names = sys.stdin.readlines()
with open(filename) as fd:
  boys = fd.readlines()
with open(filename2) as fd:
  girls = fd.readlines()
i = 0
while i < len(names):
  if names[i] in boys and names[i] not in girls:
    print names[i].strip(), "boy"
  elif names[i] in boys and names[i] in girls:
    print names[i].strip(), "either"
  else:
    print names[i].strip(), "girl"
  i = i + 1
