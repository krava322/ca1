#!/usr/bin/env python


i = 0
k = a[0]
while i < len(a) and k[:len(s)] != s:
  k = a[i]
  if k[:len(s)] == s:
    print a[i]
    i = len(a)
  i = i + 1
