#!/usr/bin/env python

s = raw_input()
b = 0
while s != "end":
  s = raw_input()
  i = 0
  while i < len(s) and s[i] != "," and s != "end":
    i = i + 1
  if s[i] == "y" and s[i - 1] == "t" and s[i - 2] == "i" and s[i - 3] == "C":
    print s[:i]
      
