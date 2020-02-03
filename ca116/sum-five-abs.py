#!/usr/bin/env python

s = 0
i = 0

while i < 5:
  b = input()
  if b < 0:
    b = b * - 1
  s = s + b
  i = i + 1
print s
