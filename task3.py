#!/usr/bin/env python

import argparse
import json

parser = argparse.ArgumentParser(description='Process summ of range')
parser.add_argument('age', type=int, help='start of the range')

args = parser.parse_args()

output_json = json.load(open('users.json'))


def valid_phone(phone):
    return len(phone) == 13 and phone[0] == "+"


def valid_email(email):
    return "@" in email and "." in email


def valid_age(current_age, ask_age):
    return ask_age <= current_age


for key, value in output_json.iteritems():
    if valid_phone(str(value.get("Phone"))) and \
       valid_email(str(value.get("Email"))) and \
       valid_age(int(value.get("Age")), args.age):
        print key
