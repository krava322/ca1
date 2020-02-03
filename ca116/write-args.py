#!/usr/bin/env python

import sys
args = sys.argv[1:]
message = ""
file_name = args[0]
i = 1
while i < len(args):
  message = message + args[i] + "\n"
  i = i + 1

with open(file_name, "w") as fd:
  fd.write(message)
