#!/usr/bin/env python

s = raw_input()
i = 0
if s[0] == s[1] and len(s) == 2:
 print s
else:
  while i < len(s):
    if s[i] == s[i - 1] and s[0] != s[len(s) -1]:
      print s[i] + s[i - 1]
      i = len(s)
    i = i + 1
