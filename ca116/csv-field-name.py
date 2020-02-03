#!/usr/bin/env python

import sys
args = sys.argv[1:]

s = raw_input()
coma = 0
i = 0
ans = ""
while coma != int(args[0]):
  if s[i] == ",":
    coma = coma + 1
  i = i + 1
while i < len(s) and s[i] != ",":
  ans = ans + s[i]
  i = i + 1
print ans
