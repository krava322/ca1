#!/usr/bin/env python

a = []
b = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
c = raw_input()
while c != "end":
  b.append(c)
  c = raw_input()

i = 0
ans = ""
while i < len(b):
  if b[i] != "":
    ans = ans + a[int(b[i])]
    ans = ans + " "
  elif b[i] == "":
    print ans[:len(ans) - 1]
    ans = ""
  i = i + 1
if ans != "":
  print ans[:len(ans) - 1]
