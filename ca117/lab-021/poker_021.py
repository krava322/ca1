#!/usr/bin/env python3

import sys

def main():
    lines = sys.stdin.readlines()
    total = len(lines)
    Nothing = 0
    One_pair = 0
    Two_pairs = 0
    Three_of_a_kind = 0
    Straight = 0
    Flush = 0
    Full_house = 0
    Four_of_a_kind = 0
    Straight_flush = 0
    Royal_flush = 0
    for line in lines:
        line = line.strip()
        if line[-1] == "0":
            Nothing += 1
        elif line[-1] == "1":
            One_pair += 1
        elif line[-1] == "2":
            Two_pairs += 1
        elif line[-1] == "3":
            Three_of_a_kind += 1
        elif line[-1] == "4":
            Straight += 1
        elif line[-1] == "5":
            Flush += 1
        elif line[-1] == "6":
            Full_house += 1
        elif line[-1] == "7":
            Four_of_a_kind += 1
        elif line[-1] == "8":
            Straight_flush += 1
        elif line[-1] == "9":
            Royal_flush += 1
    print("The probability of nothing is " + "{:.4f}".format(Nothing / total * 100) + "%")
    print("The probability of one pair is " + "{:.4f}".format(One_pair / total * 100) + "%")
    print("The probability of two pairs is " + "{:.4f}".format(Two_pairs / total * 100) + "%")
    print("The probability of three of a kind is " + "{:.4f}".format(Three_of_a_kind / total * 100) + "%")
    print("The probability of a straight is " + "{:.4f}".format(Straight / total * 100) + "%")
    print("The probability of a flush is " + "{:.4f}".format(Flush / total * 100) + "%")
    print("The probability of a full house is " + "{:.4f}".format(Full_house / total * 100) + "%")
    print("The probability of four of a kind is " + "{:.4f}".format(Four_of_a_kind / total * 100) + "%")
    print("The probability of a straight flush is " + "{:.4f}".format(Straight_flush / total * 100) + "%")
    print("The probability of a royal flush is " + "{:.4f}".format(Royal_flush / total * 100) + "%")


if __name__ == '__main__':
    main()
