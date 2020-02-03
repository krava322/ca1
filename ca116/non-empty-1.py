#!/usr/bin/env python

b = ""
i = 0
t = 0
while i < len(a):
  if a[i] != b:
    t = t + 1
  i = i + 1
print t
