#!/usr/bin/env python

s = raw_input()
i = 0
total = 0
p = ""
while i < len(s):
  if s[i] == "+":
    i = i + 1
    total = total + int(p)
    p = ""
    l = i
  p = p + s[i]
  i = i + 1
print total + int(s[l:])
