#!/usr/bin/env python

x = input()

if x % 10 == 1 and x != 11:
  print "st"
elif x % 10 == 2 and x != 12:
  print "nd"
elif x % 10 == 3 and x != 13:
  print "rd"
elif x == 11 or x == 12 or x == 13:
  print "th"
elif x == 2:
  print "nd"
elif x == 1:
  print "st"
elif x == 3:
  print "rd"
else:
  print "th"
