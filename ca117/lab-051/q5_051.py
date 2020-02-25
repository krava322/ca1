#!/usr/bin/env python3

import sys

def seconds(time):
    btime = 99999999999999999999
    for i in time:
        try:
            k = i.split(":")
            seconds = int(k[0]) * 60 + int(k[1])
            if seconds < btime:
                btime = seconds
        except ValueError:
            return "Error"
    return btime
def main():
    lines = sys.stdin.readlines()
    d = {}
    for line in lines:
        line = line.split()
        name = line[0]
        time = line[1:]
        d[name] = seconds(time)

    for i in d:
        if d[i] == "Error":
            d[i] = 9999999999999999999

    wname = min(d, key=d.get)
    wtime = d[min(d, key=d.get)]
    minutes = wtime // 60
    sec = wtime - minutes * 60
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    wtime = str(minutes) + ":" + str(sec)
    print("{} : {:3s}".format(wname, wtime))
if __name__ == '__main__':
    main()
