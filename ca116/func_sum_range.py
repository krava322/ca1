#!/usr/bin/env python

import func_bsearch

def sum_range(a, low, high):
  x = func_bsearch.bsearch(a, low)
  total = 0
  while x < len(a) and a[x] < high:
    total = total + a[x]
    x += 1
  return total
