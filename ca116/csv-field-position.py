#!/usr/bin/env python

import sys
args = sys.argv[1:]

s = raw_input()
coma = 0
i = 0

while s[i: i + len(args[0])] != str(args[0]):
  if s[i] == ",":
    coma = coma + 1
  i = i + 1

print coma
