#!/usr/bin/env python

import sys

line = sys.stdin.read().split()
i = 0
t = 0
while i < len(line):
  t = t + int(line[i])
  i = i + 1
print t
