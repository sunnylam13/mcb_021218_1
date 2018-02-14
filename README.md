# Multiple Clipboard

Py program to track many pieces of text

.pyw means Py won't show a terminal window when it runs...

prog saves each clip under a keyword...

EXAMPLE:  

run `py mcb.pyw save spam`

current clipped contents saved with keyword `spam`

to load it to clipboard, run `py mcb.pyw spam`

if user forgets, use `py mcb.pyw list` to copy all keywords
 to clipboard


## actions

command line arg for keyword is checked

if arg is `save`, clipped is saved to the keyword

if arg is `list`, all keywords copied to clipboard

else text for keyword is copied to keyboard

delete a single keyword or all keywords


## code actions

read command line arguments from sys.argv

read/write to clipboard

save and load to a shelf file

delete a keyword from the file with `delete <keyword>`

delete *all* keywords


## Windows execution

create batch file named `mcb.bat`

@pyw.exe C:\Python34\mcb.pyw %*

in Run


common practice to put general usage information in comments at the top of the file

If you ever forget how to run your script, you can always look at these comments for a reminder. Then you import your modules

Copying and pasting will require the pyperclip module

The shelve module will also come in handy: Whenever the user wants to save a new piece of clipboard text, you’ll save it to a shelf file. Then, when the user wants to paste the text back to their clipboard, you’ll open the shelf file and load it back into your program. The shelf file will be named with the prefix mcb ➌.

SAVE CLIPBOARD CONTENT

If the first command line argument (which will always be at index 1 of the sys.argv list) is 'save' ➊, 

the second command line argument is the keyword for the current content of the clipboard. 

The keyword will be used as the key for mcbShelf, and the value will be the text currently on the clipboard ➋.

If there is only one command line argument, you will assume it is either 'list' or a keyword to load content onto the clipboard. 

## References

ABSP: 312

ABSP: 318 (for extending MCB)# Password Locker Program Insecure
