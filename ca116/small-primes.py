#!/usr/bin/env python

a = input()

if a % 2 == 0 and a >= 3 or a == 1:
  print "not prime"
elif a % 3 == 0 and a >= 9:
  print "not prime"
else:
  print "prime"
