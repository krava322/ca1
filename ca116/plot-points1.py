#!/usr/bin/env python

import sys
a = "|                    |"
points = sys.stdin.readlines()
cor = {}
i = 0
biggesty = 0
biggestx = 0
while i < len(points):
  k = points[i].split(" ")
  cor[int(k[0])] = int(k[1])
  if biggestx < int(k[0]):
    biggestx = int(k[0])
  cor[int(k[0].strip())] = int(k[1].strip())
  if biggesty < int(k[1].strip()):
    biggesty = int(k[1].strip())
  i = i + 1
row = biggesty
while i < row:
  ans = ""
  if i == cor[i]:
    for i in cor[i]:
    
