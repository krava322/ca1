#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()
b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
d = {}
i = 0
while i < len(a):
  d[a[i]] = b[i]
  i = i + 1
k = 0
ans = ""
while k < len(lines):
  j = 0
  while j < len(lines[k].strip()):
    if lines[k][j] in d:
      ans += d[lines[k][j]]
    else:
      ans += lines[k][j]
    j = j + 1
  if k != len(lines) - 1:
    ans += "\n"
  k = k + 1
print ans
