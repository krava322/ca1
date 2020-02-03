#!/usr/bin/env python

import sys

d = {}
a = []
lines = sys.stdin.readlines()
i = 0
while i < len(lines):
  d[lines[i].strip()] = 0
  a.append(lines[i].strip())
  i = i + 1
for i in a:
  if i in d:
    d[i] += 1
for i in d:
  if d[i] == 1:
    print i
