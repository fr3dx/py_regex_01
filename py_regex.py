#!/usr/bin/env python3.8

# Script filters out pattern(s): XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX with the help of regex from opened file and 
# format them such: ('XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX','XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')

import re

filename = input("Enter your filename: ")
txt = ""
match = ()

def open_file():
    global txt
    try:
        with open(filename) as f:
            txt = f.read()
    except OSError:
        print("""File doesn't exists. Run the script again...""")
    else:
        return txt

open_file()

def fmt_regex(txt):
    regex = '([A-Z0-9]{8})+-([A-Z0-9]{4})+-([A-Z0-9]{4})+-([A-Z0-9]{4})+-([A-Z0-9]{12})'
    global match
    match = re.findall(regex, txt)
    return match

fmt_regex(txt)

def fmt_2(match):
    rm_tpls = ['-'.join(tups) for tups in match]
    rm_whtspc = '\',\''.join(rm_tpls)
    return rm_whtspc

if txt != "" and match != ():
    print("('"+ (fmt_2(match)) +"')")
