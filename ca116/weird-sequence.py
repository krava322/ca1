#!/usr/bin/env python

i = input()
n = 0
c = 1
while n < i:
  print n * c
  c = c * (-1)
  n = n + 1
