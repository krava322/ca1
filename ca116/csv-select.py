#!/usr/bin/env python

import sys
args = sys.argv[1:]
a = []
s = raw_input()
while s != "end":
  a.append(s)
  s = raw_input()
value = ""
header = ""
i = 0
while i < len(args[0]) and args[0][i] != "=":
  header = header + args[0][i]
  i = i + 1
if args[0][i] == "=":
  value = value + args[0][i + 1:]
coma = 0
i = 0
while i < len(a[0]) and header != a[0][i:len(header)]:
  if a[0][i] == ",":
    coma = coma + 1
  i = i + 1
i = 0
while i < len(a):
  j = 0
  coma1 = 0
  k = a[i]
  if coma != 0:
    while j < len(k) and coma1 != coma:
      if k[j] == ",":
        coma1 = coma1 + 1
      j = j + 1
      if k[j:j + len(value)] == value:
        print a[i]
  else:
    if k[:2] == value:
      print a[i]
  i = i + 1
