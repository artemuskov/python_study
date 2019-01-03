#!/usr/bin/env python

import json
import re


def valid_phone(phone):
    if phone[0] == "+":
        numbers = phone.split("+", 1)[1]
        return len(numbers) == 12 and numbers.isdigit()


def valid_email(email):
    if len(email) > 7:
        return bool(re.match(
            "^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))


def valid_age(current_age, ask_age):
    return ask_age <= current_age


def validate_user(user):
    user_data = user[1]
    requirements = [valid_phone(str(user_data.get("Phone"))),
           valid_email(str(user_data.get("Email"))),
           valid_age(user_data.get("Age"), 17)]
    if any(requirements):
        return user


def main():
    with open('users.json', 'r') as user_file:
        user_json = json.load(user_file)

    output_users = dict(map(validate_user, user_json.items()))

    with open('filtered.json', 'w') as outf:
        json.dump(output_users, outf)


if __name__ == "__main__":
    main()
