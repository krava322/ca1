#!/usr/bin/env python

i = 0
while i < len(a):
  k = a[i]
  if k[0:len(s)] == s:
    print a[i]
  i = i + 1
