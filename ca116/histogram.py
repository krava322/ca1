#!/usr/bin/env python

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
s = raw_input()

while s != "end":
  b.append(int(s))
  s = raw_input()

i = 0
while i < len(a):
  k = 0
  t = 0
  while k < len(b):
    if b[k] == a[i]:
      t = t + 1
    k = k + 1
  print a[i], t * "*"
  i = i + 1
