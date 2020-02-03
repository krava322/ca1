#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
b = input()
i = 0
pos = 0
while i < len(a):
  if a[i] <= b:
    pos = pos + 1
    i = i + 1
  else:
    i = i + 1
print pos
