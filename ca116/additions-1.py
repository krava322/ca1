#!/usr/bin/env python

t = 10
i = 0
while i < t:
  j = 0
  k = 0
  s1 = ""
  s = raw_input()
  while j < len(s) and s[j] != "+":
    s1 = s1 + s[j]
    j = j + 1
  i = i + 1
  print int(s1) + int(s[j + 1:])
