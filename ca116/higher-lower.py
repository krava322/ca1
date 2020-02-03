#!/usr/bin/env python

cur = input()
i = 0
while i < 5:
  next = input()
  if cur < next:
    print "higher"
  elif cur > next:
    print "lower"
  else:
    print "equal"
  cur = next
  i = i + 1
