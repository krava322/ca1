#!/usr/bin/env python

import sys
words = sys.stdin.readlines()
d = {}
a = []
i = 0
while i < len(words):
  a.append(words[i].strip())
  i = i + 1
i = 0
while i < len(a):
  if a[i] in d:
    print "snap:", a[i]
    i = len(a)
  else:
    d[a[i]] = a[i]
    i = i + 1
