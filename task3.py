#!/usr/bin/env python

import argparse
import json

# parser = argparse.ArgumentParser(description='Process summ of range')
# parser.add_argument('age', type=int, help='start of the range')
#
# args = parser.parse_args()

with open('users.json', 'r') as user_file:
    user_json = json.load(user_file)


def valid_phone(phone):
    return len(phone) == 13 and phone[0] == "+"


def valid_email(email):
    return "@" in email and "." in email


def valid_age(current_age, ask_age):
    return ask_age <= current_age


def validate_user(user):
    user_data = user[1]
    return valid_phone(str(user_data.get("Phone"))) and \
           valid_email(str(user_data.get("Email"))) and \
           valid_age(int(user_data.get("Age")), 30)


output_users = dict(filter(validate_user, user_json.items()))
print output_users
