#!/usr/bin/env python


a = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
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
k = 0
while k < len(a):
  print a[k]
  k = k + 1
