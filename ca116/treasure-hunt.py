#!/usr/bin/env python

import os
import sys
files = os.listdir(".")         # Line A.
file_name = "start.txt"
i = 1
while i == 1:
  with open(file_name, "r") as fd:
    line = fd.readline()
    print line
    if os.path.isfile(line):
      file_name = str(line[0])
    else:
      print line
      i = 0
