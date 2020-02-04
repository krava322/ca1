#!/usr/bin/env python3

import sys
import calendar

def main():
    year = int(sys.argv[3])
    day1 = int(sys.argv[1])
    month = int(sys.argv[2])
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    poem = ["Monday's child is fair of face.", "Tuesday's child is full of grace.", "Wednesday's child is full of woe.", "Thursday's child has far to go.", "Friday's child is loving and giving.", "Saturday's child works hard for a living.", "Sunday's child is fair and wise and good in every way."]
    print("You were born on a" + " " + day[int(calendar.weekday(year, month, day1))] + " " + "and" + " " + poem[int(calendar.weekday(year, month, day1))])
if __name__ == '__main__':
    main()
