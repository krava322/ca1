#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
i = 1
while i < len(a):
  v = a[i]
  p = i
  while 0 < p and v < a[p - 1]:
    a[p] = a[p - 1]
    p = p - 1
  a[p] = v
  i = i + 1

v = "does not matter"
n = 0

i = 0
while i < len(a):
  j = i + 1
  while j < len(a) and a[j] == a[i]:
    j = j + 1
  if n < j - i:
    n = j - i
    v = a[i]
  i = j

print v, n