#!/usr/bin/env python3

import re
import sys


def strip_r(text, chars=None):
    if chars is not None:
        regex = ''
        for char in chars:
            regex += char + '*'
        spaces = re.compile(regex)
    else:
        spaces = re.compile(r'\s*')  # this will find white spaces in a string
    striped_text = spaces.sub('', text)
    return striped_text


if __name__ == '__main__':
    text = sys.argv[1]
    if len(sys.argv) == 2:
        print('case 1')
        print(strip_r(text))
    else:
        print('case 2')
        chars = sys.argv[2]
        print(strip_r(text, chars))
