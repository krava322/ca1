#!/usr/bin/env python

s = input()
i = 0
ans = ""
while s != 0:
  if s % 2 == 1:
    s = s / 2
    ans = str("1") + ans
  elif s % 2 == 0:
    ans = str("0") + ans
    s = s / 2
print ans
