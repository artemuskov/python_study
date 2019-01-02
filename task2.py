#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Process summ of range')
parser.add_argument('start', type=int, help='start of the range')
parser.add_argument('end', type=int, help='end of the range')
args = parser.parse_args()


def summarize(x, y):
    return x + y


try:
    print(reduce(summarize, range(args.start, args.end+1)))
except Exception as e:
    print('end parameter must be greater then start')
