#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
b = input()
a.append(b)
i = 1
while i < len(a):
  v = a[i]
  p = i
  while 0 < p and v < a[p - 1]:
    a[p] = a[p - 1]
    p = p - 1
  a[p] = v
  i = i + 1
print a
