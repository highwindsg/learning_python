#!/usr/bin/env python3
# phoneAndEmail.py - Finds phone numebers and email addresses pn the clipboard.

import pyperclip, re

phoneRegex = re.compiler(r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )""", re.VERBOSE)

# TODO: Create email regex.
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )""", re.VERBOSE)

# TODO: Find matches in clipboard text.
#
# TODO: Copy results to the clipboard.

