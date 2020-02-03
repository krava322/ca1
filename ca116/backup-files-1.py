#!/usr/bin/env python

import os
import sys
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
  file_name = str(files[i])
  if files[i][len(files[i]) - 4:] != ".bak":
    with open(file_name, "r") as fd:
      lines = fd.read()
      if len(lines) != 0:
        with open(file_name + ".bak", "w") as fd:
          fd.write(lines)
  i = i + 1
