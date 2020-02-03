#!/usr/bin/env python

import sys
file_name = "a.txt"
file_name2 = "b.txt"
d = {}
inter = 0
with open(file_name) as fd:
  lines = fd.readlines()
  i = 0
  while i < len(lines):
    key = lines[i].strip()
    d[key] = key
    i = i + 1
with open(file_name2) as fd:
  lines1 = fd.readlines()
  i = 0
  while i < len(lines1):
    if lines1[i].strip() in d:
      inter = 1
    i = i + 1
if inter == 1:
  print "intersecting"
else:
  print "disjoint"
