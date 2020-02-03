#!/usr/bin/env python


a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]
i = 0
b = a[i]
while i < len(a):
  if a[i - 1] < a[i]:
    b = a[i]
  i = i + 1
