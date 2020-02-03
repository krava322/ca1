#!/usr/bin/env python

import os
files = os.listdir(".")         # Line A.

i = 0
while i < len(files):
  file_name = str(files[i])
  if files[i][len(files[i]) - 3:] == ".py":
    with open(file_name, "r") as fd:
      lines = fd.readlines()
      if len(lines) != 0:
        print files[i]
  with open(file_name, "r") as fd:
    line = fd.readline()
    if line == "#!/usr/bin/env python\n":
      print files[i]

  i = i + 1
