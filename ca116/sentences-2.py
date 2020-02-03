#!/usr/bin/env python

import sys

s = sys.stdin.read()

words = s.split()

i = 0
ans = ""
while i < len(words):
  if words[i][-1] == "." or words[i][-1] == "?" or words[i][-1] == "!":
    ans += words[i] + "\n"
  else:
    ans += words[i] + " "
  i += 1

ans_list = ans.split("\n")
i = 0
while i < len(ans_list) - 1:
  sentence = ""
  ans_words = ans_list[i].split()
  j = 0
  if ans_words[0] > "A" and ans_words[0] < "Z":
    sentence += ans_words[j] + " "
    j += 1
  else:
    sentence += ans_words[0].capitalize() + " "
    j += 1
  while j < len(ans_words) - 1:
    sentence += ans_words[j] + " "
    j += 1
  sentence += ans_words[j]
  print sentence
  i += 1 
