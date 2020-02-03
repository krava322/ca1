#!/usr/bin/env python

a = raw_input()
b = raw_input()
c = raw_input()

if len(a) > len(b) and len(a) > len(c):
  print a
elif len(b) > len(a) and len(b) > len(c):
  print b
elif len(c) > len(b) and len(c) > len(a):
  print c
