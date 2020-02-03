#!/usr/bin/env python

s = 0
i = 1

while i != 0:
  b = input()
  if b < 0:
    b = b * - 1
  s = s + b
  i = i + 1
  if b == 0:
    i = 0
print s
