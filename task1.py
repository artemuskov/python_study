#!/usr/bin/env python


def devide_by_number(inpt, dev):
    return inpt % dev == 0


for i in range(1, 101):
    if devide_by_number(i, 15):
        print "fizzbuzz"
    elif devide_by_number(i, 5):
        print "buzz"
    elif devide_by_number(i, 3):
        print "fizz"
    else:
        print i
