#!/usr/bin/env python

s = raw_input()
i = 0
r = ""
t = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
  i = i + 1
if i != len(s):
  t = i
j = i
while j < len(s) and s[j] >= "0" and s[j] <= "9":
  r = r + s[j]
  j = j + 1
if t != 0:
  print r, t
