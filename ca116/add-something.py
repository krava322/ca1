#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
  a.append(int(s))
  s = raw_input()
i = 0
n = input()
while i < len(a):
  a[i] = a[i] + n
  print a[i]
  i = i + 1
