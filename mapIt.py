#! python3
# mapIt.py - Launches a map in the browser using and address from the command 
# line or clipboard.

import webbrowser, sys, pyperclip, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    address.replace(" ", "+")
    logging.DEBUG(address)
    
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/' + address)