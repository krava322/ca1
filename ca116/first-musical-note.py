#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
  if s[i] == "a" or s[i] == "b" or s[i] == "c" or s[i] == "d":
    print s[i]
    i = i + len(s)
  elif s[i] == "e" or s[i] == "f" or s[i] == "g":
    print s[i]
    i = i + len(s)
  i = i + 1
