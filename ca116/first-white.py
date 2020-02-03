#!/usr/bin/env python

s = raw_input()
i = 0
t = 0
b = " "
while i < len(s):
  if s[i] == b:
    print t
    i = len(s)
  i = i + 1
  t = t + 1
if t == len(s):
  print "-1"
