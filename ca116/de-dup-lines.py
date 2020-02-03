#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
  i = 0
  while i < len(a) and a[i] != s:
    i = i + 1
  if i == len(a):
    a.append(s)
  s = raw_input()
k = 0
while k < len(a):
  print a[k]
  k = k + 1
