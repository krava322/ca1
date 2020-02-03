#!/usr/bin/env python

import sys
file_name = "irish-dobs.txt"
with open(file_name, "r") as fd:
  lines = fd.read()
  print lines
