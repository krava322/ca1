#!/usr/bin/env python

s = raw_input()
i = 0
r = ""
t = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
  i = i + 1
if i < len(s):
  t = i
j = i
while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
  r = r + s[j]
  j = j + 1
if t == 0 and not ("a" <= s[0] and s[0] <= "z"):
  print r, t
if t != 0:
  print r, t
