#!/usr/bin/env python

s = raw_input()
i = 0
t = 0
while i < len(s):
  if "A" <= s[i] and s[i] <= "Z":
    print s[i], t
    i = len(s)
  i = i + 1
  t = t + 1
