#!/usr/bin/env python

s = 0
i = 1

while i != 0:
  b = input()
  s = s + b
  i = i + 1
  if b == 0:
    i = 0
print s
