#!/usr/bin/env Python3
"""Saves and loads content(text) to the clipboard
	Usage:
		pyhton mcb.py save <keyword>	- Saves the current content of the
						clipboard to the keyword.
		python mcb.py <keyword>	- Loads the content of the keyword
						to the clipboard.
		python mcb.py list		- Loads a list containing all the
						keywords to the clipboard.
		pyhton mcb.py delete <keyword>	- Deletes the content within the
						the specified keyword.
		python mcb.py deleteAll	- Deletes all the stored contents in the shelf
						file.
"""
import shelve
import pyperclip
import sys

shelfFile = shelve.open('mcb')  # we create a shelf file to store the clipboard
# content, so we can retrieve it later.

# save the clipboard cotent.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
    	shelfFile[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
    	try:
    	    del shelfFile[sys.argv[2]]
    	except KeyError as e:
    		print('Error, the key %s was not found' % e)
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(shelfFile.keys())))
    elif sys.argv[1].lower() == 'del_all':
    	shelfFile.clear()
    	print('Clear')
    elif sys.argv[1] in shelfFile:
        pyperclip.copy(shelfFile[sys.argv[1]])

shelfFile.close()