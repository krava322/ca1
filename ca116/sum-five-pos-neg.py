#!/usr/bin/env python

s = 0
i = 0
f = 0
while i < 5:
  b = input()
  if b < 0:
    f = f + b
  if b > 0:
    s = s + b
  i = i + 1
print f, s
