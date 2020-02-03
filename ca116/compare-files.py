#!/usr/bin/env python

import sys
args = sys.argv[1:]
file_name = args[0]
file_name1 = args[1]
with open(file_name, "r") as fd:
  lines = fd.readlines()
with open(file_name1, "r") as fd:
  lines1 = fd.readlines()

i = 0
while i < len(lines) and i < len(lines1):
  j = 0
  while j < len(lines[i]) and lines[i][j] == lines1[i][j]:
    j = j + 1
  if j != len(lines[i]):
    print i, j
    i = len(lines)
  i = i + 1
if len(lines) < len(lines1):
  print len(lines), 0
if len(lines) > len(lines1):
  print len(lines1), 0
