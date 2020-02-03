#!/usr/bin/env python

s = ""
while s != "end":
  s = raw_input()
  i = 0
  while i < len(s) and s[i] != "," and s != "end":
    i = i + 1
  if s[i + 1] == "W" and s[i + 2] == "I":
      print s[:i]
