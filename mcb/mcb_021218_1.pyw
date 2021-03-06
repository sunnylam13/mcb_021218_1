# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# Usage: 
# python3 mcb_021218_1.pyw save <keyword> - saves clipboard to keyword
# python3 mcb_021218_1.pyw <keyword> - loads keyword to clipboard
# python3 mcb_021218_1.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#####################################
# SAVE CLIPBOARD CONTENT
#####################################

# Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# List keywords and load content
	if sys.argv[1].lower() == 'list': # if only 1 arg, check if list
		pyperclip.copy(str(list(mcbShelf.keys()))) # if so, list of shelf keys copied to clipboard, user can paste list later
	elif sys.argv[1] in mcbShelf: # assume command line arg is a keyword...  if it exists in the mcbShelf file as a key...
		pyperclip.copy(mcbShelf[sys.argv[1]]) # ...load value onto the clipboard

#####################################
# END SAVE CLIPBOARD CONTENT
#####################################

mcbShelf.close()

