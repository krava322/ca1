#!/usr/bin/env python

import sys

args = sys.argv[1:]
i = 0
t = 0
while i < len(args):
  file_name = args[i]
  with open(file_name, "r") as fd:
    line = fd.read().split()
    k = 0
    while k < len(line):
      t = t + int(line[k])
      k = k + 1
  i = i + 1
print t
