#!/usr/bin/env python

s = raw_input()
b = "QWERTYUIOPASDFGHJKLZXCVBNM"
i = 0
c = 0
while i < len(s):
  while c < len(b):
    if b[c] == s[i]:
      i = i + len(s)
      print b[c]
    c = c + 1
  i = i + 1
print b[c]
