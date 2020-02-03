#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()
d = {}
a = []
i = 0
while i < len(lines):
  pair = lines[i].split(".")
  d[pair[0] + "." + pair[1]] = pair[2].strip()
  if (pair[0] + "." + pair[1]) not in a:
    a.append(pair[0] + "." + pair[1])
  i = i + 1
i = 0
while i < len(d):
  if d[a[i]] == "correct":
    print a[i]
  i = i + 1
