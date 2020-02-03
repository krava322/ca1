#!/usr/bin/env python


import sys
file_name = "translation.txt"
with open(file_name, "r") as fd:
  words = fd.readlines()
print words
