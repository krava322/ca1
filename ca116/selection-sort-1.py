#!/usr/bin/env python

j = 1
p = 0
a = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
while j < len(a):
  if a[j] < a[p]:
    p = j
  j = j + 1
print p
