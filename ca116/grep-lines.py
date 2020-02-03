#!/usr/bin/env python

import sys
args = sys.argv[1:]

a = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
i = 0
while i < len(a):
  b = a[i]
  k = 0
  while k < len(b):
    if b[k:k + len(args[0])] == args[0]:
      print a[i]
    k = k + 1
  i = i + 1
