#!/usr/bin/env python


a = []
b = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
s = raw_input()
while s != "end":
  b.append(s)
  s = raw_input()
i = 0
while i < len(a) + len(b):
  j = 0
  while j < len(a):
    k = b[i]
    c = a[i]
    if k == c[0:8]
      print c[9:]
    j = j + 1
  i = i + 1