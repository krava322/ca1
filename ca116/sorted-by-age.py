#!/usr/bin/env python


a = []
s = raw_input()
while s != "end":
  s = s[6:8] + s[3:5] + s[0:2] + s[9:]
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
  c = a[k]
  print c[6:]
  k = k + 1
