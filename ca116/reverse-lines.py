#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
i = 0
while i < len(a):
  print a[len(a) - 1 - i]
  i = i + 1
