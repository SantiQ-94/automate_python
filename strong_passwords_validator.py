#!/usr/bin/env python3

import re
import sys

numberRegex = re.compile(r'[0-9]')
lowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')


def validate(_pass):
    if len(_pass) >= 8:
        numberFlag = numberRegex.findall(_pass)
        lowerFlag = lowerRegex.findall(_pass)
        upperFlag = upperRegex.findall(_pass)
        if (len(numberFlag) > 0) and (
                len(lowerFlag) > 0) and (len(upperFlag) > 0):
            print('The password is strong enough.')
        else:
            print('The password is a little bit weak.')
    else:
        print('The password is not 8 characters long.')


if __name__ == '__main__':
    _pass = sys.argv[1]
    validate(_pass)
