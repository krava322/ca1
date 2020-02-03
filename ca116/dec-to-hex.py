#!/usr/bin/env python

s = input()
i = 0
ans = ""
base = 16
while s != 0:
  if s % base == 1:
    s = s / base
    ans = str(s % base) + ans
  elif s % base == 0:
    ans = str("0") + ans
    s = s / base
print ans
