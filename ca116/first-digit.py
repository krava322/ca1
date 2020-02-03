#!/usr/bin/env python

s = raw_input()
i = 0
t = 0
while i < len(s):
  if "0" <= s[i] and s[i] <= "9":
    print s[i], t
    i = len(s)
  i = i + 1
  t = t + 1
