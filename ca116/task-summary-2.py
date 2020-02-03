#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()
d = {}
d1 = {}
i = 0
while i < len(lines):
  usr = lines[i].split("/")
  d[usr[0]] = 0
  i = i + 1

i = 0
while i < len(lines):
  usr = lines[i].split("/")
  usr[1] = usr[1].split(".")
  d1[usr[0] + " " + usr[1][0] + "." + usr[1][1]] = usr[1][2].strip()
  i = i + 1

for i in d:
  for j in d1:
    k = j.split(" ")
    if d1[j] == "correct" and k[0] == i:
      d[i] += 1

for i in d:
  print i, d[i]
