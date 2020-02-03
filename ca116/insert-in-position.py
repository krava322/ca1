#!/usr/bin/env python


a = []
k = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
b = input()
i = 0
while i < len(a) and b >= a[i]:
  k.append(a[i])
  i = i + 1
k.append(b)
while i < len(a) and b < a[i]:
  k.append(a[i])
  i = i + 1
c = 0
while c < len(k):
  print k[c]
  c = c + 1
