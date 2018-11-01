#!/usr/bin/env python3

# Just like dictionary, shelf values have keys() and values() methods that
# will return list-like values of keys and values in the shelf.
# Since these methods return list-like values instead of true lists, you
# should pass them to the list() function to get them in list form.

# Enter the following into the interactive shell to see the results.

import shelve

shelfFile = shelve.open("mydata")
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()
