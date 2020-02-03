#!/usr/bin/env python

import secret_number
n = 1000
def play():
  hig = 1000
  low = 0
  i = 0
  while i < 10:
    g = secret_number.guess((hig + low) / 2)
    if g == "too-high":
      hig = (hig + low) / 2
    elif g == "too-low":
      low = (hig + low) / 2
    i = i + 1
