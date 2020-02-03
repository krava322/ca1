#!/usr/bin/env python

a = input()
b = input()
c = input()

if a + b > c and a + c > b and c + b > a:
  print "yes"
else:
  print "no"
