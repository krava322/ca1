#!/usr/bin/env python


import sys
fruits = sys.stdin.readlines()
fruit = {
  "apple\n": True,
  "pear\n": True,
  "orange\n": True,
  "banana\n": True,
  "cherry\n": True,
}
i = 0
while i < len(fruits):
  if fruits[i] in fruit:
    print fruits[i].strip()
  i = i + 1
