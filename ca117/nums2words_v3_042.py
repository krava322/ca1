#!/usr/bin/env python3

import sys
s = sys.stdin.readlines()
def get_key(val):
    for key, value in d.items():
         if val == value:
             return key


d = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
nd = {}
with open(sys.argv[1]) as fd:
    fd = fd.readlines()
for i in fd:
    i = i.split()
    if i[0] in d.values():
        nd[get_key(i[0])] = i[1]
for line in s:
    line = line.split()
    ans = ""
    for number in line:
        if number in nd:
            ans += nd[number] + " "
    print(ans[:-1])
