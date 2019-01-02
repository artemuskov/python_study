#!/usr/bin/env python


def devide_by_number(inpt, dev):
    if inpt % dev == 0:
        return True


for i in range(1, 101):
    if devide_by_number(i, 15):
        print "fizzbizz"
        continue
    if devide_by_number(i, 5):
        print "bizz"
        continue
    if devide_by_number(i, 3):
        print "fizz"
        continue
    print i