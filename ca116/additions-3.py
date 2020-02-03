#!/usr/bin/env python

b = 0
while b != 1:
  j = 0
  k = 0
  s1 = ""
  s = raw_input()
  while j < len(s) and s[j] != "+":
    s1 = s1 + s[j]
    j = j + 1

  print int(s1) + int(s[j + 1:])
  if int(s1) + int(s[j + 1:]) == 1000:
    j = len(s)
    b = 1
