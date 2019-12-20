#!/usr/bin/python

import random
import sys

_alnum = [c for c in range(256) if chr(c).isalnum()]

def genpwd (length=8, charset=_alnum):
    pwd = ''
    for i in range(length):
        pwd += chr(random.choice(charset))
    return pwd


if __name__ == '__main__':
    if len (sys.argv) < 2:
        r = genpwd ()
    elif len (sys.argv) < 3:
        r = genpwd (int (sys.argv[1]))
    else:
        r = genpwd (int (sys.argv[1]), eval(sys.argv[2]))
    print r
