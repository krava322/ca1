#!/usr/bin/env python

import sys
args = sys.argv[1:]
i = 0
t = 0
while i < len(args):
  file_name = args[i]
  with open(file_name, "r") as fd:
    text = fd.readlines()
  j = 0
  while j < len(text):
    t = t + int(text[j])
    j = j + 1
  i = i + 1
print t
