#!/usr/bin/env python3

import sys

def most(a):
    return "Words with most e's: {}".format([w.strip() for w in a if all(w.lower().count("e") >= x.lower().count("e") for x in a)])

def main():
    s = sys.stdin.readlines()
    shortestv = [x.strip() for x in s if all(c in x for c in ["a", "e", "i", "o", "u"])]
    print("Words containing 17 letters:", [x.strip() for x in s if len(x.strip()) == 17])
    print("Words containing 18+ letters:", [x.strip() for x in s if len(x.strip()) >= 18])
    print("Shortest word containing all vowels: {}".format(min(shortestv, key=len)))
    print("Words with 4 a's:", [x.strip() for x in s if x.lower().count("a") == 4])
    print("Words with 2+ q's:", [x.strip() for x in s if x.lower().count("q") >= 2])
    print("Words containing cie:", [x.strip() for x in s if "cie" in x])
    print("Anagrams of angle:", [x.strip() for x in s if len(x.strip()) == 5 and "a" in x.lower() and "n" in x.lower() and "g" in x.lower() and "l" in x.lower() and "e" in x.lower() and x.strip().lower() != "angle"])
    print("Words ending in iary:", len([x for x in s if x[len(x) - 5:] == "iary\n"]))
    print(most(s))
if __name__ == '__main__':
    main()
