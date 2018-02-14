# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# Usage: 
# python3 mcb_021218_2.pyw save <keyword> - saves clipboard to keyword
# python3 mcb_021218_2.pyw <keyword> - loads keyword to clipboard
# python3 mcb_021218_2.pyw list - loads all keywords to clipboard

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

#####################################
# DELETE CLIPBOARD CONTENT
#####################################

# Delete the specific keyword and its data
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2]] # remove the specific key and value specified in the 2nd arg
# Delete all of the keywords
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
	mcbShelf.clear() # remove all of the keys and values in the dict

#####################################
# END DELETE CLIPBOARD CONTENT
#####################################

mcbShelf.close()

#####################################
# DOCUMENTATION
#####################################

# Multi-clipboard
# ABSP: 312
# ABSP: 318 (for extending MCB)

# Py program to track many pieces of text
# .pyw means Py won't show a terminal window when it runs...
# prog saves each clip under a keyword...
# EXAMPLE:  
# run `py mcb.pyw save spam`
# current clipped contents saved with keyword `spam`
# to load it to clipboard, run `py mcb.pyw spam`
# if user forgets, use `py mcb.pyw list` to copy all keywords to clipboard

# actions
# command line arg for keyword is checked
# if arg is `save`, clipped is saved to the keyword
# if arg is `list`, all keywords copied to clipboardd
# else text for keyword is copied to keyboard
# delete a single keyword or all keywords

# code actions
# read command line arguments from sys.argv
# read/write to clipboard
# save and load to a shelf file
# delete a keyword from the file with `delete <keyword>`
# delete *all* keywords

# Windows execution
# create batch file named `mcb.bat`
# @pyw.exe C:\Python34\mcb.pyw %*
# in Run

# common practice to put general usage information in comments at the top of the file
# If you ever forget how to run your script, you can always look at these comments for a reminder. Then you import your modules

# Copying and pasting will require the pyperclip module

# The shelve module will also come in handy: Whenever the user wants to save a new piece of clipboard text, you’ll save it to a shelf file. Then, when the user wants to paste the text back to their clipboard, you’ll open the shelf file and load it back into your program. The shelf file will be named with the prefix mcb ➌.

# SAVE CLIPBOARD CONTENT
# If the first command line argument (which will always be at index 1 of the sys.argv list) is 'save' ➊, 
# the second command line argument is the keyword for the current content of the clipboard. 
# The keyword will be used as the key for mcbShelf, and the value will be the text currently on the clipboard ➋.
# If there is only one command line argument, you will assume it is either 'list' or a keyword to load content onto the clipboard. 



#####################################
# END DOCUMENTATION
#####################################