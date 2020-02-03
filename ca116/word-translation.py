#!/usr/bin/env python

import sys
words = sys.stdin.readlines()
translation = {}
with open("translation.txt") as fd:
  lines = fd.readlines()
  i = 0
  while i < len(lines):
    pair = lines[i].split()
    translation[pair[0]] = pair[1]
    i = i + 1
i = 0
while i < len(words):
  if words[i].strip() in translation:
    print translation[words[i].strip()]
  i = i + 1
