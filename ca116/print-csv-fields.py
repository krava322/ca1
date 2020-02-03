#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
whichcoma = input()

i = 0
while i < len(a):
  coma = 0
  pos1 = 0
  j = 0
  k = a[i]
  while j < len(k) and whichcoma != coma:
    if k[j] == ",":
      coma = coma + 1
    pos1 = pos1 + 1
    j = j + 1
  pos2 = pos1
  while j < len(k) and k[j] != ",":
    pos2 = pos2 + 1
    j = j + 1
  print k[pos1:pos2]
  i = i + 1
