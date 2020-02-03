#!/usr/bin/env python


a = []
b = []
c = []
s = raw_input()
while s != "end":
  b.append(int(s))
  s = raw_input()
s = raw_input()
while s != "end":
  c.append(int(s))
  s = raw_input()
i = 0
while i < len(b):
  a.append(b[i])
  i = i + 1
i = 0
while i < len(c):
  a.append(c[i])
  i = i + 1
i = 0
while i < len(a):
  p = i
  j = i + 1
  while j < len(a):
    if a[j] < a[p]:
      p = j
    j = j + 1

  tmp = a[p]
  a[p] = a[i]
  a[i] = tmp
  i = i + 1
i = 0
while i < len(a):
  print a[i]
  i = i + 1
