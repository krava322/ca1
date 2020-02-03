#!/usr/bin/env python

import sys
file_name = "irish-dobs.txt"
file_name2 = "american-dobs.txt"
with open(file_name, "r") as fd:
  lines = fd.readlines()
with open(file_name2, "w") as fd:
  i = 0
  while i < len(lines):
    d = 0
    m = 0
    j = 0
    while j < len(lines[i]) and lines[i][j] != "/":
      d = d + 1
      j = j + 1
    j = j + 1
    m = d
    while j < len(lines[i]) and lines[i][j] != "/":
      m = m + 1
      j = j + 1
    if m == 4:
      m1 = m - 1
      fd.write(lines[i][m1:m + 1] + "/" + lines[i][:d] + lines[i][m + 1:])
    elif m == 3 and d != 2:
      m1 = m - 1
      fd.write(lines[i][m1:m + 1] + "/" + lines[i][:d] + lines[i][m + 1:])
    else:
      fd.write(lines[i][m] + "/" + lines[i][:d] + lines[i][m + 1:])
    i = i + 1
