#!/usr/bin/env python

mark = input()


print "first:", mark >= 70
print "second:", 69 >= mark and mark >= 50
print "third:", 49 >= mark and mark >= 40
print "fail:", mark < 40
