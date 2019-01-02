#!/usr/bin/env python


def devide_by(input):
    if input % 3 == 0:
        print "fizz"
    if input % 5 == 0:
        print "bizz"
    if input % 15:
        print "fizzbizz"
    print i


for i in range(1, 101):
    devide_by(i)