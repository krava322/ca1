#!/usr/bin/env python

s = raw_input()
f = ""
i = 0
while i < len(s):
  f = f + s[len(s) - 1 - i]
  i = i + 1
print f
