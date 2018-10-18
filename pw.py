#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {"email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
             "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
             "luggage": "12345"}

import sys, pyperclip

# The cmd line arg will be stored in the variable 'sys.argv'.
# The first item in the 'sys.argv' list should always be a string containing
# the program's filename (eg. 'pw.py'), and the second should be the first
# cmd line argument. Therefore length should be less than 2.
if len(sys.argv) < 2:

# Since the cmd line arg is mandatory, you display a usage message to the user
# if they forget to add it (that is, if the 'sys.argv' list has fewer than two
# values in it).
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account + ".")

