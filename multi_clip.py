#!/usr/bin/env python3
import shelve
import pyperclip
import os
import argparse


def save(keyword, shelfFile):
    shelfFile[keyword] = pyperclip.paste()


def delete(keyword, shelfFile):
    del shelfFile[keyword]


def get_clipboard(keyword, shelfFile):
    if keyword in shelfFile:
        pyperclip.copy(shelfFile[keyword])
    else:
        print('The keyword was not found.')


def clear(shelfFile):
    shelfFile.clear()
    print('Shelf file cleared.')


def _list(shelfFile):
    pyperclip.copy(str(list(shelfFile.keys())))


if __name__ == '__main__':
    shelfFile = shelve.open('mcb')
    choices = {'clear': clear, 'list': _list}
    parser = argparse.ArgumentParser(description='Saves and loads text to be '
                                     'used with the clipboard.')
    parser.add_argument('-d', type=str, metavar='Deletes <keyword>',
        help='Deletes a keyword entry and the content asociated with it.')
    parser.add_argument('-r', metavar='Retrieves <keyword>', help='Retrieves '
                        'the content associated with the keyword.')
    parser.add_argument('-s', type=str, metavar='Saves <keyword>',
        help='Saves the current content of the clipboard to the keyword.')
    parser.add_argument('-f', choices=choices,
        help='Function to be performed; either CLEAR all the keywords stored '
        'or LIST them.')

    args = parser.parse_args()
    if args.f:
        function = choices[args.f]
        function(shelfFile)
    elif args.d:
        delete(args.d, shelfFile)
    elif args.r:
        get_clipboard(args.r, shelfFile)
    elif args.s:
        save(args.s, shelfFile)
    shelfFile.close()
