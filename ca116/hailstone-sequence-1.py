#!/usr/bin/env python

i = input()
n = 1
c = input()
print c
while n < i:
  if c % 2 == 0:
    print c / 2
    c = c / 2
  elif c % 2 != 0:
    print c * 3 + 1
    c = c * 3 + 1
  n = n + 1
