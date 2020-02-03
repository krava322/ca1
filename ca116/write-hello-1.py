#!/usr/bin/env python

import sys
args = sys.argv[1:]

file_name = args[0]
message = "Hello world."
with open(file_name, "w") as fd:
  fd.write(message)
  fd.write("\n")
