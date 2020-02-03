#!/usr/bin/env python

a = []
b = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
c = raw_input()
while c != "end":
  b.append(int(c))
  c = raw_input()
i = 0
while i < len(b):
  print a[b[i]]
  i = i + 1
