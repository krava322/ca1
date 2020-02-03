#!/usr/bin/env python

import sys
args = sys.argv[1:]
file_name = args[0]
with open(file_name, "r") as fd:
  text = fd.readlines()
t = 0
i = 0
while i < len(text):
  t = t + int(text[i])
  i = i + 1
print t
