#!/usr/bin/env python

n = input()

prev = 0
curr = 1

i = 0
print prev
while i < n:
  if prev < n:
    tmp = curr
    curr = prev + curr
    prev = curr - prev
    if prev < n:
      print prev
  i = i + 1
