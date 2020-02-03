#!/usr/bin/env python

import sys
file_name = "a.txt"
file_name2 = "b.txt"
d = {}
with open(file_name) as fd:
  lines = fd.readlines()
  i = 0
  while i < len(lines):
    key = lines[i].strip()
    d[key] = key
    i = i + 1
with open(file_name2) as fd:
  lines = fd.readlines()
  i = 0
  while i < len(lines):
    key = lines[i].strip()
    d[key] = key
    i = i + 1
for i in d:
  print i
