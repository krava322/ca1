#!/usr/bin/env python

import func_bsearch

def count(a, q):
  p = func_bsearch.bsearch(a, q)
  c = func_bsearch.bsearch(a, q + 1)
  return c - p
