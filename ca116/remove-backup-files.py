#!/usr/bin/env python

import os
import sys
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
  file_name = files[i]
  if files[i][len(files[i]) - 4:] == ".bak":
    if os.path.isfile(file_name):
      os.unlink(file_name)
  i = i + 1
