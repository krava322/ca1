#!/usr/bin/env python

n = input()

prev = 0
curr = 1

i = 0
while i < n:
   print prev
   tmp = curr
   curr = prev + curr
   prev = curr - prev
   i = i + 1
