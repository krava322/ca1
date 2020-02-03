#!/usr/bin/env python

import sys
filename = "boys.txt"
filename2 = "girls.txt"
d = {}
boys = []
girls = []
with open(filename) as fd:
  lines = fd.readlines()
  
i = 0
while i < len(lines):
  d[lines[i].strip()] = 0
  boys.append(lines[i].strip())
  i += 1
with open(filename2) as fd:
  lines1 = fd.readlines()
i = 0
while i < len(lines1):
  d[lines1[i].strip()] = 0
  girls.append(lines1[i].strip())
  i += 1
for i in d:
  if i in boys and i not in girls:
    print i, "boy"
  elif i in boys and i in girls:
    print i, "either"
  else:
    print i, "girl"
