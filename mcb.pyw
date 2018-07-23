#!/usr/bin/env Python3
"""Saves and loads content(text) to the clipboard
	Usage:
		pyhton mcb.pyw save <keyword> - Saves the current content of the
										clipboard to the keyword.
		python mcb.pyw <keyword>	  - Loads the content of the keyword
										to the clipboard.
		python mcb.pyw list			  - Loads a list containing all the
										keywords to the clipboard.		
"""
import shelve, pyperclip, sys

shelfFile = shelve.open('mcb')	#we create a shelf file to store the clipboard
								#content, so we can retrieve it later.

#save the clipboard cotent.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	shelfFile[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	#verify if the list method was called
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(shelfFile.keys())))
	elif sys.argv[1] in shelfFile:
		pyperclip.copy(shelfFile[sys.argv[1]])

shelfFile.close()
