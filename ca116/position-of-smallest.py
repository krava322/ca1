#!/usr/bin/env python


a = []
k = []
s = raw_input()
while s != "end":
  a.append(int(s))
  s = raw_input()
b = input()
i = 0
while i < len(a):
  if a[i] <= b:
    k.append(a[i])
  elif b > a[i]:
    k.append(b)
    k.append(a[i])
  i = i + 1
  
