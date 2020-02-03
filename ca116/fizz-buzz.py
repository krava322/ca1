#!/usr/bin/env python

i = input()
n = 1
while n <= i:
  if n % 3 == 0 and n % 5 != 0:
    print "fizz"
  elif n % 5 == 0 and n % 3 != 0:
    print "buzz"
  elif n % 5 == 0 and n % 3 == 0:
    print "fizz-buzz"
  else:
    print n
  n = n + 1
